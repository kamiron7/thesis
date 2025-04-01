import requests


class BaseClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

    def _request(
            self,
            method: str,
            endpoint: str,
            **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        return response
