import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
import pytest
import allure
from api.pages.cart_page import CartPage
from api.pages.bookmarks_page import BookmarksPage

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
credentials_path = os.path.join(project_root, "config", "credentials.json")

with open(credentials_path) as f:
    credentials = json.load(f)
    BASE_URL = credentials["base_url"]
    TOKEN = credentials["token"]


@pytest.fixture
def cart_page():
    return CartPage(BASE_URL, TOKEN)


@pytest.fixture
def bookmarks_page():
    return BookmarksPage(BASE_URL, TOKEN)


@allure.epic("API Tests")
@allure.feature("Cart Operations")
class TestCartPositive:
    @allure.story("Add product to cart")
    @allure.title("Successfully add product to cart")
    def test_add_product_to_cart(self, cart_page):
        response = cart_page.add_product(
            2405917,
            {"item_list_name": "product-page"}
        )
        assert response.status_code == 200

    @allure.story("Update product quantity")
    @allure.title("Successfully update product quantity in cart")
    def test_update_product_quantity(self, cart_page):
        add_response = cart_page.add_product(
            2405917,
            {"item_list_name": "product-page"}
        )
        assert add_response.status_code == 200

        cart_item_id = cart_page.get_cart_item_id(2405917)
        assert cart_item_id is not None

        response = cart_page.update_quantity(cart_item_id, 5)
        assert response.status_code == 200

    @allure.story("Remove product from cart")
    @allure.title("Successfully remove product from cart")
    def test_remove_product_from_cart(self, cart_page):
        add_response = cart_page.add_product(
            2405917,
            {"item_list_name": "product-page"}
        )
        assert add_response.status_code == 200

        cart_item_id = cart_page.get_cart_item_id(2405917)
        assert cart_item_id is not None

        response = cart_page.remove_product(cart_item_id)
        assert response.status_code == 204


@allure.epic("API Tests")
@allure.feature("Cart Operations")
class TestCartNegative:
    @allure.story("Add non-existent product")
    @allure.title("Attempt to add non-existent product to cart")
    def test_add_non_existent_product(self, cart_page):
        response = cart_page.add_product(
            32626326,
            {"item_list_name": "product-page"}
        )
        assert response.status_code == 500

    @allure.story("Update product quantity")
    @allure.title("Attempt to update product quantity beyond available amount")
    def test_update_quantity_beyond_available(self, cart_page):
        response = cart_page.update_quantity(156135754, 999)
        assert response.status_code == 422

    @allure.story("Remove non-existent product")
    @allure.title("Attempt to remove non-existent product from cart")
    def test_remove_non_existent_product(self, cart_page):
        response = cart_page.remove_product(4536634)
        assert response.status_code == 404


@allure.epic("API Tests")
@allure.feature("Bookmarks Operations")
class TestBookmarksPositive:
    @allure.story("Add product to bookmarks")
    @allure.title("Successfully add product to bookmarks")
    def test_add_product_to_bookmarks(self, bookmarks_page):
        response = bookmarks_page.add_product(2820265)
        assert response.status_code == 201


@allure.epic("API Tests")
@allure.feature("Bookmarks Operations")
class TestBookmarksNegative:
    @allure.story("Add non-existent product")
    @allure.title("Attempt to add non-existent product to bookmarks")
    def test_add_non_existent_product_to_bookmarks(self, bookmarks_page):
        response = bookmarks_page.add_product(52623626)
        assert response.status_code == 500
