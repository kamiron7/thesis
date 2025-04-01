# E-commerce Test Automation Framework

## Overview
This project is a test automation framework designed to test both API and UI functionalities of an e-commerce platform. The framework implements automated tests for critical features such as shopping cart operations and bookmarks management.

## Project Structure
```
├── api/
│   └── pages/         # Page object models for API testing
├── config/
│   └── credentials.json   # Configuration and credentials
├── test/
│   ├── test_api.py   # API test cases
│   └── test_ui.py    # UI test cases
└── requirements.txt   # Project dependencies
```

## Features
- API Testing:
  - Shopping Cart Operations
    - Adding products to cart
    - Updating product quantities
    - Removing products from cart
  - Bookmarks Operations
    - Adding products to bookmarks
  - Both positive and negative test scenarios

- UI Testing (in development)

## Technologies
- Python 3.x
- Pytest - Testing framework
- Selenium - Web UI testing
- Requests - HTTP library for API testing
- Allure - Test reporting

## Prerequisites
- Python 3.x
- pip (Python package installer)

## Installation
1. Clone the repository:
```bash
git clone <repository-url>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure credentials:
- Create a `credentials.json` file in the `config` directory with the following structure:
```json
{
    "base_url": "your_base_url",
    "token": "your_api_token"
}
```

## Running Tests
To run API tests:
```bash
pytest test/test_api.py
```

To run UI tests:
```bash
pytest test/test_ui.py
```

To generate Allure reports:
```bash
pytest --alluredir=./allure-results
allure serve allure-results
```

## Test Structure
- Tests are organized using the Page Object Model pattern
- API tests are grouped by feature (Cart, Bookmarks)
- Each feature has both positive and negative test scenarios
- Test cases are documented using Allure annotations for better reporting 