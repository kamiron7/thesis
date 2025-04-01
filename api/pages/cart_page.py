from api.base_client import BaseClient
import allure
import json


class CartPage(BaseClient):
    @allure.step("Add product to cart")
    def add_product(self, product_id: int, ad_data: dict = None) -> dict:
        data = {"id": product_id}
        if ad_data:
            data["adData"] = ad_data
        response = self._request(
            "POST",
            "/api/v1/cart/product",
            json=data
        )
        return response

    @allure.step("Get cart items")
    def get_cart_items(self) -> list:
        response = self._request("GET", "/api/v1/cart")
        try:
            return response.json().get("products", [])
        except json.JSONDecodeError:
            return []

    @allure.step("Get cart item ID by product ID")
    def get_cart_item_id(self, product_id: int) -> int:
        try:
            cart_items = self.get_cart_items()
            if not isinstance(cart_items, list):
                return None
            for item in cart_items:
                if (isinstance(item, dict) and
                        item.get("goodsId") == product_id):
                    return item.get("id")
            return None
        except Exception:
            return None

    @allure.step("Update product quantity in cart")
    def update_quantity(self, cart_item_id: int, quantity: int) -> dict:
        data = [{"id": cart_item_id, "quantity": quantity}]
        response = self._request("PUT", "/api/v1/cart", json=data)
        return response

    @allure.step("Remove product from cart")
    def remove_product(self, cart_item_id: int) -> dict:
        response = self._request(
            "DELETE",
            f"/api/v1/cart/product/{cart_item_id}"
        )
        return response
