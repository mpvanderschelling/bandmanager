#                                                                       Modules
# =============================================================================

# Standard

# Local
from .constants import VAT_HIGH, VAT_LOW

# Third-party

#                                                        Authorship and Credits
# =============================================================================
__author__ = "Martin van der Schelling (mpvanderschelling@gmail.com)"
__credits__ = ["Martin van der Schelling"]
__status__ = "Stable"
# =============================================================================
#
# =============================================================================


class Item:
    def __init__(
        self,
        description: str,
        price: int,
        quantity: int = 1,
        vat_rate: float = VAT_LOW,
    ):
        self.description = description
        self.price = price
        self.quantity = quantity
        self.vat_rate = vat_rate

    @property
    def total_price(self) -> int:
        return self.price * self.quantity

    def is_empty(self) -> bool:
        return not self.description

    def to_dict(self) -> dict:
        return {
            "name": self.description,
            "price": self.price / 100,
            "quantity": self.quantity,
            "total_price": self.total_price / 100,
        }


class LineItems:
    def __init__(self, line_items):
        self.line_items: list[Item] = line_items

    @classmethod
    def from_list_of_dicts(cls, list_of_dicts: list):
        return cls([Item(**_dict) for _dict in list_of_dicts])

    @property
    def sub_total(self) -> int:
        return sum(item.total_price for item in self.line_items)

    @property
    def vat_low(self) -> int:
        return sum(
            item.total_price * item.vat_rate
            if item.vat_rate == VAT_LOW
            else 0.0
            for item in self.line_items
        )

    @property
    def vat_high(self) -> int:
        return sum(
            item.total_price * item.vat_rate
            if item.vat_rate == VAT_HIGH
            else 0.0
            for item in self.line_items
        )

    @property
    def total(self) -> int:
        return self.sub_total + self.vat_low + self.vat_high

    def add(self, item: Item):
        self.line_items.append(item)

    def to_dict(self) -> dict:
        return {
            "line_items": [
                item.to_dict()
                for item in self.line_items
                if not item.is_empty()
            ],
            "sub_total": self.sub_total / 100,
            "vat_low": self.vat_low / 100,
            "vat_high": self.vat_high / 100,
            "total": round(self.total / 100, 2),
        }
