class Product:
    """The Product class represents a product in the store.
    Methods:
    - get_quantity(): Returns the quantity of the product.
    - set_quantity(quantity): Sets the quantity of the product. If the quantity
     reaches 0, the product is deactivated.
    - is_active(): Returns True if the product is active, otherwise False.
    - activate(): Activates the product.
    - deactivate(): Deactivates the product.
    - show(): Returns a string representation of the product.
    - buy(quantity): Buys a given quantity of the product and returns the total
     price of the purchase."""
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("name cannot be empty")
        if price < 0:
            raise ValueError("price cannot be negative")
        if quantity <= 0:
            raise ValueError("quantity cannot be negative or zero")
        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True

    def get_quantity(self) -> float:
        """Returns the quantity (float)"""
        return self._quantity

    def set_quantity(self, quantity: int):
        """Setter function for quantity. If quantity reaches 0,
        deactivates the product."""
        if quantity < 0:
            raise ValueError("quantity cannot be negative")
        self._quantity = quantity
        if not self._quantity:
            self._active = False

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
        return f"{self._name}, Price: {self._price}," \
               f" Quantity: {self._quantity}"

    def buy(self, quantity: int) -> float:
        """Buys a given quantity of the product.
        Returns the total price (float) of the purchase"""
        if quantity > self._quantity:
            raise ValueError("quantity has to be equal or less "
                             "to the quantity of the product")

        # deactivate product if it reached 0
        self._quantity -= quantity
        if self._quantity == 0:
            self.deactivate()

        total_price = self._price * quantity
        return total_price
