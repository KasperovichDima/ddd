"""TDD Example."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Self

from core.exceptions import OutOfStock


@dataclass(frozen=True)
class OrderLine:
    """A single line of order representation."""

    orderid: str
    sku: str
    qty: int


class Batch:
    """Batch of some product."""

    def __init__(
        self, ref: str, sku: str, qty: int, eta: date | None
    ) -> None:
        """Batch initialization."""
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchase_quantity = qty
        self._allocations: set[OrderLine] = set()

    def allocate(self, line: OrderLine) -> None:
        """Reduce batch size according to the order."""
        if self.can_allocate(line):
            self._allocations.add(line)

    def can_allocate(self, line: OrderLine) -> bool:
        """Check if order line can be allocated."""
        return self.sku == line.sku and self.available_quantity >= line.qty

    def deallocate(self, line: OrderLine) -> None:
        """Cancel order line allocation."""
        if line in self._allocations:
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        """Total allocated quantity."""
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        """Quantity available to purchase."""
        return self._purchase_quantity - self.allocated_quantity

    def __gt__(self, other: Self) -> bool:
        """Compare this batch with other by eta date."""
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta

    def __eq__(self, other: object) -> bool:
        """Check if this batch is equivalent to other batch."""
        if not isinstance(other, Self):
            return False
        return self.reference == other.reference

    def __hash__(self) -> int:
        return hash(self.reference)


def allocate(line: OrderLine, batches: list[Batch]) -> str:
    """Get batch ref to allocate order line."""
    try:
        batch = next(b for b in sorted(batches) if b.can_allocate(line))
        batch.allocate(line)
    except StopIteration:
        raise OutOfStock from None
    return batch.reference
