from products import Product


class Store:
    """This class represents a store with a list of products."""
    def __init__(self, store_products: list[Product]):
        self._products = store_products

    def __contains__(self, item):
        return item in self._products

    def add_product(self, product: Product):
        """Adding product to the list of products in the store"""
        self._products.append(product)

    def remove_product(self, product):
        """Removes a product from store"""
        try:
            self._products.remove(product)
        except ValueError:
            pass

    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total."""
        total_quantity = sum(prod.get_quantity() for prod in self._products)
        return total_quantity

    def get_all_products(self) -> list[Product]:
        """Returns all products in the store that are active"""
        active_product = [prod for prod in self._products
                          if prod.is_active()]
        return active_product

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """Buys the products and returns the total price of the order.
        :param
        shopping_list: list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        """
        store_products = self.get_all_products()
        total_price = 0

        # buying product if it in the store, and it has required quantity
        for order_product, quantity_to_buy in shopping_list:
            total_price += order_product.buy(quantity_to_buy)

        return total_price

