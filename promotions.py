import abc


class Promotion(abc.ABC):
    """
    Abstract base class for promotions.

    This class defines the common interface for promotions. Subclasses must
    provide an implementation for the abstract method `get_promotion_discount()`,
    which calculates the total price after applying the discount.

    Attributes:
        _name (str): The name of the promotion.
    """
    def __init__(self, name):
        self._name = name

    @abc.abstractmethod
    def apply_promotion(self, quantity: int, price: float) -> float:
        """
        Calculate the total price after applying the promotion discount.

        Args:
            quantity (int): The quantity of items being purchased.
            price (float): The original price of each item.

        Returns:
            float: The total price after applying the discount.
        """
        pass


class SecondHalfPrice(Promotion):
    """represent promotion that reduces the price
    of every second item in the purchased quantity by 50%."""
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, quantity: int, price: float) -> float:
        """
        Calculate the total price after applying the promotion discount.

        For the SecondHalfPrice promotion, every second item is priced at
        50% off, while the remaining items are priced at the original price.

        Args:
            quantity (int): The quantity of items being purchased.
            price (float): The original price of each item.

        Returns:
            float: The total price after applying the discount.
        """
        discount = 0.5
        full_price_items = (quantity + 1) // 2
        discounted_items = quantity - full_price_items

        total_price = (full_price_items * price +
                       discounted_items * price * discount)

        return round(total_price, 2)


class PercentDiscount(Promotion):
    """
      A class representing a percentage-based discount promotion.

      Attributes:
          name (str): The name of the promotion.
          percent (float): The percentage discount to apply.

      Raises:
          ValueError: If the percent discount value is not
           between 0 and 100 (inclusive).

      """
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        if 0 <= percent <= 100:
            self._percent = percent
        else:
            raise ValueError("Wrong percent discount value")

    def apply_promotion(self, quantity: int, price: float) -> float:
        """
        Applies the percentage discount to the given quantity and price.

        Args:
            quantity (int): The quantity of items.
            price (float): The price of each item.

        Returns:
            float: The total price after applying the discount.

        """
        total_price = quantity * price
        total_price_discount = total_price * ((100 - self._percent)/100)
        return round(total_price_discount, 2)


class ThirdOneFree(Promotion):
    """
    A class representing a "Buy Two, Get One Free" promotion.

    Attributes:
        name (str): The name of the promotion.
    """
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, quantity: int, price: float) -> float:
        """
        Calculates the total price after applying the
        "Buy Two, Get One Free" offer.

        Parameters:
            quantity (int): Represents the total number of items bought.
            price (float): Represents the cost of a single item.

        Returns:
            float: The final cost after applying the
                "Buy Two, Get One Free" promotion.
        """
        amount_of_free_products = quantity // 3
        amount_of_products_to_pay = quantity - amount_of_free_products
        total_price = amount_of_products_to_pay * price
        return round(total_price, 2)

