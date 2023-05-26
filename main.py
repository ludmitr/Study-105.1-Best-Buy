import products
import store
import sys


def start():
    """ This function starts the main program loop. The user is presented
    with a menu of options to interact with the store. This loop continues
    until the user decides to quit."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
        ]
    best_buy = store.Store(product_list)
    while True:
        print_menu()
        user_input = input("Please choose a number: ")
        execute_user_input(user_input, best_buy)


def execute_user_input(user_input: str, store_best_buy: store.Store) -> None:
    """
    This function executes the corresponding functionality based on the
    user's input.

    :param store_best_buy: represent class store with products
    :param user_input: The user's input choice.
    :return: None
    """
    menu_functions_dict = {
        "1": print_all_products_in_store,
        "2": print_total_amount_in_store,
        "3": make_an_order,
        "4": quit_the_programm,
    }
    if user_input in menu_functions_dict:
        menu_functions_dict[user_input](store_best_buy)


def print_all_products_in_store(store_best_buy: store.Store):
    all_products = store_best_buy.get_all_products()

    # printing
    print("-"*10)
    for store_product in all_products:
        print(store_product.show())
    print("-"*10)


def print_total_amount_in_store(store_best_buy: store.Store):
    print("-"*10)
    total_amount = store_best_buy.get_total_quantity()
    print(f"Total of {total_amount} items in store")
    print("-"*10)


def make_an_order(store_best_buy: store.Store):
    """Allows the user to make an order by
    selecting products and quantities."""
    all_products: list[products.Product] = store_best_buy.get_all_products()
    print_products_list(all_products)

    orders: dict[products.Product, int] =\
        get_quantities_of_products_from_user(all_products)

    # creating list_order by running on orders
    list_order = [(product, quantity) for product, quantity in orders.items()]

    try:
        price_paid = store_best_buy.order(list_order)
    except ValueError as e:
        print(e)
        return

    if price_paid:
        print("*" * 8)
        print(f"Order made! Total payment: {price_paid}")


def get_quantities_of_products_from_user(all_products: list) -> dict:
    """
    Returns a dictionary where the key is a Product and the value
    is the quantity chosen by the user. Quit the loop if both inputs are
    empty.

    :param all_products: List of all products available in the store.
    :return: Dictionary with Product as key and chosen quantity as value.
    """
    orders = {}
    while True:
        user_number_input = input("Which product # do you want? ")
        user_amount_input = input("What amount do you want? ")

        # case quitting loop
        if not user_number_input and not user_amount_input:
            break

        # validate user input,
        message = "Product added to the list"
        try:
            product_to_buy, quantity = validate_user_input(user_number_input,
                                                           user_amount_input,
                                                           all_products, orders)
            # adding product and quantity to orders dict
            if product_to_buy in orders:
                orders[product_to_buy] += quantity
            else:
                orders[product_to_buy] = quantity

        except(IndexError, ValueError):
            message = "Error adding product!"
        print(message)

    return orders


def validate_user_input(user_number_input: str, user_amount_input: str,
                        all_products: list, orders: dict):
    """validating user input. if the input is invalid -
    it will raise an error, otherwise it will return
    a tuple of product name:str and quantity: int"""
    product_index = int(user_number_input) - 1

    if product_index not in range(len(all_products)):
        raise ValueError("Wrong index")
    product_to_buy = all_products[product_index]
    quantity = int(user_amount_input)
    if quantity <= 0:
        raise ValueError

    return product_to_buy, quantity

def print_products_list(all_products):
    """Printing list of items for make_an_order func"""
    print("-" * 10)
    for index, store_product in enumerate(all_products, start=1):
        print(f"{index} {store_product.show()}")
    print("-" * 10)
    print("When you want to finish order, enter empty text.")


def quit_the_programm(*args):
    print("BYE")
    sys.exit()


def print_menu():
    """Printing menu for main programm"""
    menu_to_print = "   Store Menu\n"\
                    "   ----------\n"\
                    "1. List of all products\n"\
                    "2. Show total amount in store\n"\
                    "3. Make an order\n"\
                    "4. Quit\n"
    print(menu_to_print)


if __name__ == '__main__':

    start()
