from __future__ import annotations


class GxYoga:
    """
    A GxYoga person

    GxYoga's salary is different from others since they are not part of the
    company.

    Salary is calculated based on the "amount of classes" and
    "price per class"

    === Attributes ===
    amount: The amount classes that the teacher taught for the whole month

    === Representation invariants ===
    amount and price per class are non-negative numbers
    """
    amount: int
    price: float

    def __init__(self, name: str, amount: int, price: int) -> None:
        """
        Initialize the receptionist

        Precondition: fixed_salary must be a non-negative float
        """
        self.name = name
        self.amount = amount
        self.price = price

    def get_fixed_salary(self) -> float:
        """
        Get the total salary of one month for the security

        hour_of_work: the amount of hours the security worked for a month
        """
        return self.amount * self.price
