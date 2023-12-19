"""Value-objects example."""
from __future__ import annotations

from typing import NamedTuple


class Money(NamedTuple):  # noqa: D101
    currency: str
    value: int

    def __add__(self, other: Money) -> Money:
        if other.currency != self.currency:
            raise ValueError(f"Cannot add {self.currency} to {other.currency}")
        return Money(self.currency, self.value + other.value)

    def __sub__(self, other: Money) -> Money:
        if self.currency != other.currency:
            raise TypeError(f'Can not subtract {other.currency} from {self.currency}!')
        return Money(self.currency, self.value - other.value)

    def __mul__(self, multiplier: int) -> Money:
        if isinstance(multiplier, Money):
            raise TypeError
        return Money(self.currency, self.value * multiplier)
