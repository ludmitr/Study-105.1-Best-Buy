import products
import pytest


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
    test_product.set_quantity(0)
    assert not test_product.is_active()

    # checking case when i buy product and amount left is 0
    test_product = products.Product("tv", 22.5, 1)
    test_product.buy(1)
    assert not test_product.is_active()


def test_purchase_modify_quantity():
    """test that buying product modify quantity of a product"""
    test_product = products.Product("tv", 22.5, 110)
    test_product.buy(100)
    assert test_product.get_quantity() == 10


def test_buy_larger_quantity():
    """Test that buying a larger quantity than exists invokes exception"""
    with pytest.raises(ValueError, match="Error while making order! "
                                         "Quantity larger than what exists"):
        test_product = products.Product("tv", 22.5, 110)
        test_product.buy(120)


pytest.main()
