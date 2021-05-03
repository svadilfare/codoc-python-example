from dataclasses import dataclass
from enum import Enum, auto


def add_one(number):
    return number + 1


class Foo:
    ...


@dataclass
class User:

    name: str
    email: str


@dataclass
class Category:

    label: str


@dataclass
class Item:
    """
    Something you can buy
    """

    label: str
    description: str
    category: Category


@dataclass
class ShippingInformation:
    class Types:
        EXPRESS = auto()
        NORMAL = auto()
        SLOW = auto()

    shipping_type: Types


@dataclass
class Purchase:
    creator: User
    item: Item
    shipping: ShippingInformation
