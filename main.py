import products
import store
import sys


def start(my_store: store.Store):
    while True:
        print_menu()
        user_input = input("Please choose a number: ")
        execute_user_input(user_input)

def execute_user_input(user_input: str) -> None:
    """
   This function executes the corresponding functionality based on the user's input.

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
        menu_functions_dict[user_input]()

def print_all_products_in_store():
    all_products = best_buy.get_all_products()

    # printing
    print("-"*10)
    for store_product in all_products:
        print(store_product.show())
    print("-"*10)

def print_total_amount_in_store():
    print("-"*10)
    total_amount = best_buy.get_total_quantity()
    print(f"Total of {total_amount} items in store")
    print("-"*10)

def make_an_order():
    all_products = best_buy.get_all_products()
    print_products_list(all_products)

    orders: dict = get_quantities_of_products_from_user(all_products)

    list_order = []
    for product, quantity in orders.items():
        if product.get_quantity() < quantity:
            print("Error while making order! Quantity larger than what exists")
            return
        list_order.append((product, quantity))

    price_paid = best_buy.order(list_order)
    if price_paid != 0:
        print("*"*8)
        print(f"Order made! Total payment: {price_paid}")


def get_quantities_of_products_from_user(all_products: list) -> dict:
    """Returns dict where key is Product and val is quantity"""
    orders = {prod: 0 for prod in all_products}
    while True:
        user_number_input = input("Which product # do you want? ")
        user_amount_input = input("What amount do you want? ")
        if not user_number_input and not user_amount_input:
            break
        message = "Product added to the list"
        try:
            product_index = int(user_number_input)-1
            if product_index not in range(len(all_products)):
                raise ValueError
            product_to_buy = all_products[product_index]
            quantity = int(user_amount_input)
            if quantity < 0:
                raise ValueError
            if product_to_buy in orders:
                orders[product_to_buy] += quantity
        except(IndexError, ValueError):
            message = "Error adding product!"
        print(message)

    return orders


def print_products_list(all_products):
    """Printing list of items for make_an_order func"""
    print("-" * 10)
    for index, store_product in enumerate(all_products, start=1):
        print(f"{index} {store_product.show()}")
    print("-" * 10)
    print("When you want to finish order, enter empty text.")


def quit_the_programm():
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
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store(product_list)
    start(best_buy)
