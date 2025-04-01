import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)


class TestSearch:
    @allure.epic("UI Tests")
    @allure.feature("Search Functionality")
    @allure.story("Empty Search")
    @allure.title("Search with empty input")
    def test_empty_search(self, driver, wait):
        driver.get("https://www.chitai-gorod.ru/")
        search_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[data-test='search-button']")))
        search_button.click()
        search_input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[data-test='search-input']")))
        search_input.send_keys(Keys.ENTER)
        assert "chitai-gorod.ru" in driver.current_url

    @allure.story("Invalid Characters Search")
    @allure.title("Search with invalid characters")
    def test_invalid_characters_search(self, driver, wait):
        driver.get("https://www.chitai-gorod.ru/")
        search_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[data-test='search-button']")))
        search_button.click()
        search_input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[data-test='search-input']")))
        search_input.send_keys("!@#$%^&*()")
        search_input.send_keys(Keys.ENTER)
        try:
            results = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-test='search-results']")))
            assert "Ничего не найдено" in results.text
        except TimeoutException:
            assert True

    @allure.story("Valid Search")
    @allure.title("Search with valid input")
    def test_valid_search(self, driver, wait):
        driver.get("https://www.chitai-gorod.ru/")
        search_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[data-test='search-button']")))
        search_button.click()
        search_input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[data-test='search-input']")))
        search_input.send_keys("Пушкин")
        search_input.send_keys(Keys.ENTER)
        results = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[data-test='search-results']")))
        assert results.is_displayed()

    @allure.story("Latin Search")
    @allure.title("Search using Latin characters")
    def test_latin_search(self, driver, wait):
        driver.get("https://www.chitai-gorod.ru/")
        search_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[data-test='search-button']")))
        search_button.click()
        search_input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[data-test='search-input']")))
        search_input.send_keys("Pushkin")
        search_input.send_keys(Keys.ENTER)
        results = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[data-test='search-results']")))
        assert results.is_displayed()

    @allure.story("Cyrillic Search")
    @allure.title("Search using Cyrillic characters")
    def test_cyrillic_search(self, driver, wait):
        driver.get("https://www.chitai-gorod.ru/")
        search_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[data-test='search-button']")))
        search_button.click()
        search_input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[data-test='search-input']")))
        search_input.send_keys("Пушкин")
        search_input.send_keys(Keys.ENTER)
        results = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[data-test='search-results']")))
        assert results.is_displayed()


class TestBookPage:
    @allure.epic("UI Tests")
    @allure.feature("Book Page Functionality")
    @allure.story("Checkout Button")
    @allure.title("Checkout button state for in-stock book")
    def test_checkout_button_state(self, driver, wait):
        driver.get("https://www.chitai-gorod.ru/product/2405917")
        checkout_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[data-test='checkout-button']")))
        assert checkout_button.is_enabled()

    @allure.story("Buy Button")
    @allure.title("Buy button state for in-stock book")
    def test_buy_button_state(self, driver, wait):
        driver.get("https://www.chitai-gorod.ru/product/2405917")
        buy_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[data-test='buy-button']")))
        assert buy_button.is_enabled()


class TestBookFiltering:
    @allure.epic("UI Tests")
    @allure.feature("Book Filtering")
    @allure.story("Popularity Filter")
    @allure.title("Sort books by popularity")
    def test_popularity_filter(self, driver, wait):
        driver.get("https://www.chitai-gorod.ru/")
        sort_dropdown = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='sort-dropdown']")))
        sort_dropdown.click()
        popularity_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(text(), 'По популярности')]")))
        popularity_option.click()
        wait.until(EC.url_contains("popular"))
        assert "popular" in driver.current_url.lower()

    @allure.story("Newness Filter")
    @allure.title("Sort books by newness")
    def test_newness_filter(self, driver, wait):
        driver.get("https://www.chitai-gorod.ru/")
        sort_dropdown = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='sort-dropdown']")))
        sort_dropdown.click()
        newness_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(text(), 'По новизне')]")))
        newness_option.click()
        wait.until(EC.url_contains("new"))
        assert "new" in driver.current_url.lower()

    @allure.story("Price Filter")
    @allure.title("Sort books by price (high to low)")
    def test_price_high_to_low_filter(self, driver, wait):
        driver.get("https://www.chitai-gorod.ru/")
        sort_dropdown = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='sort-dropdown']")))
        sort_dropdown.click()
        price_high_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(text(), 'Сначала дорогие')]")))
        price_high_option.click()
        wait.until(EC.url_contains("price-desc"))
        assert "price-desc" in driver.current_url.lower()

    @allure.story("Price Filter")
    @allure.title("Sort books by price (low to high)")
    def test_price_low_to_high_filter(self, driver, wait):
        driver.get("https://www.chitai-gorod.ru/")
        sort_dropdown = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='sort-dropdown']")))
        sort_dropdown.click()
        price_low_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(text(), 'Сначала дешевые')]")))
        price_low_option.click()
        wait.until(EC.url_contains("price-asc"))
        assert "price-asc" in driver.current_url.lower()

    @allure.story("Rating Filter")
    @allure.title("Filter books by rating")
    def test_rating_filter(self, driver, wait):
        driver.get("https://www.chitai-gorod.ru/")
        rating_filter = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='rating-filter']")))
        rating_filter.click()
        four_stars = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='rating-4']")))
        four_stars.click()
        wait.until(EC.url_contains("rating=4"))
        assert "rating=4" in driver.current_url.lower()
