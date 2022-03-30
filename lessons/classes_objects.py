"""Example of a class and object instantiation."""


class Pizza:
    """Models the idea of a Pizza."""

    # Attribute Definitions
    size: str = "small"
    toppings: int = 0
    extra_cheese: bool = False

    def __init__(self, size: str, toppings: int, extra_cheese: bool):
        """Constructor definition for initialization of attributes."""
        self.size = size
        self.toppings = toppings
        self.extra_cheese = extra_cheese

    def price(self, tax: float) -> float:
        """Calculate the price of a Pizza."""
        total: float = 0
        if self.size == "large":
            total += 10
        else:
            total += 8

        total += self.toppings * .75

        if self.extra_cheese:
            total += 1

        total *= tax

        return total


a_pizza: Pizza = Pizza("large", 3, False)
print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price(1.05)}")


another_pizza: Pizza = Pizza("small", 0, True)
print(a_pizza.size)
print(f"Price: ${another_pizza.price(1.05)}")