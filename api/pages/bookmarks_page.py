from api.base_client import BaseClient
import allure


class BookmarksPage(BaseClient):
    @allure.step("Add product to bookmarks")
    def add_product(self, product_id: int) -> dict:
        data = {"id": product_id}
        response = self._request("POST", "/api/v1/bookmarks", json=data)
        return response
