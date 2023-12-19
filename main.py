"""TDD Example."""
from datetime import date

from core import (
    Batch,
    OrderLine,
    OrderReference,
    Quantity,
    Reference,
    Sku,
    allocate,
)


def get_batch(ref: str, sku: str, qty: int, eta: date | None) -> Batch:
    return Batch(
        Reference(ref),
        Sku(sku),
        Quantity(qty),
        eta
    )

def get_order_line(id: str, sku: str, qty: int) -> OrderLine:
    return OrderLine(
        OrderReference(id),
        Sku(sku),
        Quantity(qty)
    )


tomorrow = date.fromisoformat('2023-09-26')
today = date.fromisoformat('2023-09-25')
later = date.fromisoformat('2024-01-01')

batch = get_batch("batch1", "SMALL-FORK", 10, eta=today)
allocate(get_order_line("order1", "SMALL-FORK", 10), [batch])

allocate(get_order_line("order2", "SMALL-FORK", 1), [batch])