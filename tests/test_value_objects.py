"""Value-objects test."""
from dataclasses import dataclass

import pytest

from core import Money

fiver = Money('gbp', 5)
tenner = Money('gbp', 10)


def test_equality():  # noqa: ANN201, D103
    assert Money('gbp', 10) == Money('gbp', 10)

def test_can_add_money_values_for_the_same_currency():  # noqa: ANN201, D103
    assert fiver + fiver == tenner

def test_can_subtract_money_values():  # noqa: ANN201, D103
    assert tenner - fiver == fiver

def test_adding_different_currencies_fails():  # noqa: ANN201, D103
    with pytest.raises(ValueError):
        Money('usd', 10) + Money('gbp', 10)

def test_can_multiply_money_by_a_number():  # noqa: ANN201, D103
    assert fiver * 5 == Money('gbp', 25)

def test_multiplying_two_money_values_is_an_error():  # noqa: ANN201, D103
    with pytest.raises(TypeError):
        tenner * fiver


@dataclass(frozen=True)
class Name:
    first_name: str
    surname: str

class Person:

    def __init__(self, name: Name):
        self.name = name


def test_barry_is_harry():
    harry = Person(Name("Harry", "Percival"))
    barry = harry

    barry.name = Name("Barry", "Percival")

    assert harry is barry and barry is harry
