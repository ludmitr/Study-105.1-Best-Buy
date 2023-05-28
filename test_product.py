import products
import pytest
import promotions
import store


def test_creating_instance():
    product = products.Product("tv", 22.5, 100)
    assert isinstance(product, products.Product)


def test_creating_prod_invalid_details():
    """checking if empty name, negative price or negative/0 quanitity will
    raise the right exceptions"""
    with pytest.raises(ValueError, match="name cannot be empty"):
        products.Product("", 22.5, 100)

    with pytest.raises(ValueError, match="price cannot be negative"):
        products.Product("tv", -22.5, 100)

    with pytest.raises(ValueError,
                       match="quantity cannot be negative"):
        products.Product("tv", 22.5, -100)


def test_prod_becomes_inactive():
    """checking if is_active will return False when product hit
    0 quantity"""
    # checking case when i set quantity to 0
    test_product = products.Product("tv", 22.5, 1)
    test_product.quantity = 0
    assert not test_product.is_active()

    # checking case when i buy product and amount left is 0
    test_product = products.Product("tv", 22.5, 1)
    test_product.buy(1)
    assert not test_product.is_active()


def test_purchase_modify_quantity():
    """test that buying product modify quantity of a product"""
    test_product = products.Product("tv", 22.5, 110)
    test_product.buy(100)
    assert test_product.quantity == 10


def test_buy_larger_quantity():
    """Test that buying a larger quantity than exists invokes exception"""
    with pytest.raises(ValueError, match="Error while making order! "
                                         "Quantity larger than what exists"):
        test_product = products.Product("tv", 22.5, 110)
        test_product.buy(120)

def test_property_promotion():
    """testing get/set/del property"""
    test_prod = products.Product("tv", 22.5, 110)
    test_prom = promotions.ThirdOneFree("Third One Free!")
    test_prod.promotion = test_prom
    assert test_prod.promotion.get_name() == "Third One Free!"
    assert test_prod.promotion


def test_property_quantity():
    """Test property quantity for NonStockedProduct """
    test_prod = products.NonStockedProduct("tv", 22.5)
    test_prod.quantity = 10
    assert not test_prod.quantity, "checking that quantity is 0"


def test_property_price():
    """negative price raise an error"""
    test_prod = products.NonStockedProduct("tv", 22.5)

    with pytest.raises(ValueError, match="price cannot be negative"):
        test_prod.price = - 100

    assert test_prod.price == 22.5


def test_magic_methods():
    """Testing magic methods of product"""
    # setup initial stock of inventory
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)
    bose = products.Product("Bose QuietComfort Earbuds", price=250,
                            quantity=500)
    pixel = products.Product("Google Pixel 7", price=500, quantity=250)
    windw = products.NonStockedProduct("Windows 8", price=200)
    best_buy = store.Store([mac, bose])

    assert str(mac) == mac.show()
    assert str(windw) == windw.show(), "subclasses print the right represent"
    assert bose < mac
    assert mac > bose
    assert mac in best_buy
    assert pixel not in best_buy



pytest.main()
