import promotions


class Product:
    """The Product class represents a product in the store."""
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("name cannot be empty")
        if price < 0:
            raise ValueError("price cannot be negative")

        self._name = name
        self._price = price
        self.__set_quantity(quantity)
        self._active = True
        self._promotion: promotions.Promotion = None

    def get_promotion(self):
        """returns list[Promotion] of promotions of the class"""
        return self._promotion

    def set_promotion(self, product_promotion: promotions.Promotion):
        """Set the promotions for the product"""
        self._promotion = product_promotion

    def get_quantity(self) -> int:
        """Returns the quantity (int)"""
        return self._quantity

    def set_quantity(self, quantity: int):
        """Setter function for quantity. If quantity reaches 0,
        deactivates the product."""
        if quantity < 0:
            raise ValueError("quantity cannot be negative")
        self._quantity = quantity
        if not self._quantity:
            self._active = False

    __set_quantity = set_quantity

    def is_active(self) -> bool:
        """Returns True if the product is active, otherwise False."""
        return self._active

    def activate(self):
        """Activates the product."""
        self._active = True

    def deactivate(self):
        """Deactivates the product."""
        self._active = False

    def show(self) -> str:
        """Returns a string that represents the product"""
        product_representation = f"{self._name}, Price: {self._price}," \
                                 f" Quantity: {self._quantity}"

        # adding promotions if there is any
        if self._promotion:
            product_representation += f", Promotion: {self._promotion.get_name()}"

        return product_representation

    def buy(self, quantity: int) -> float:
        """Buys a given quantity of the product.
        Returns the total price (float) of the purchase"""
        if quantity > self._quantity:
            raise ValueError("Error while making order! "
                             "Quantity larger than what exists")

        # assign total_price
        if self._promotion:
            total_price = self._promotion.apply_promotion(self._quantity,
                                                          self._price)
        else:
            total_price = self._price * quantity

        # deactivate product if it reached 0
        self._quantity -= quantity
        if self._quantity == 0:
            self.deactivate()

        return total_price


class NonStockedProduct(Product):
    """Not physical product. quantity always stays 0 """
    _QUANTITY = 0

    def __init__(self, name: str, price: float):
        super().__init__(name, price, NonStockedProduct._QUANTITY)

    def set_quantity(self, quantity):
        """quantity always stays 0, you cannot change quantity of not
        physical product"""
        pass

    def get_quantity(self) -> int:
        """returns quantity of product"""
        return NonStockedProduct._QUANTITY

    def buy(self, quantity: int) -> float:
        """Buys a given quantity of the product.
        Returns the total price (float) of the purchase"""
        # calculate total price
        prom = self.get_promotion()
        if prom:  # case when there is promotion
            total_price = prom.apply_promotion(self._quantity, self._price)
        else:
            total_price = self._price * quantity

        return total_price

    def show(self):
        """Returns a string that represents the product"""
        product_representation = f"{self._name}, Price: {self._price}," \
                                 f" Quantity: Unlimited"

        # adding promotions if there is any
        prom = self.get_promotion()
        if prom:
            product_representation += f", Promotion: {prom.get_name()}"

        return product_representation


class LimitedProduct(Product):
    """this product can be purchased maximum amount of times in an order"""
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self._maximum = maximum

    def buy(self, quantity: int) -> float:
        """Buys a given quantity of the product.
        Returns the total price (float) of the purchase"""
        if quantity > self._maximum:
            raise ValueError(f"Product {self._name} can be purchased"
                             f" {self._maximum} times")
        if quantity > self._quantity:
            raise ValueError("Error while making order! "
                             "Quantity larger than what exists")

        # calculate total price
        prom = self.get_promotion()
        if prom:  # case when there is promotions
            total_price = prom.apply_promotion(self._quantity, self._price)
        else:
            total_price = self._price * quantity

        # deactivate product if it reached 0
        self._quantity -= quantity
        if self._quantity == 0:
            self.deactivate()

        return total_price
