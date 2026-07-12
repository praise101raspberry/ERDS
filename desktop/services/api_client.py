import requests

BASE_URL = "http://127.0.0.1:8000"


class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.token = None

    def set_token(self, token: str):
        self.token = token

    def _headers(self):
        headers = {
            "Content-Type": "application/json"
        }

        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        return headers

    def login(self, username, password):
        response = requests.post(
            f"{self.base_url}/auth/login",
            json={
                "username": username,
                "password": password
            },
            headers=self._headers()
        )

        response.raise_for_status()

        data = response.json()
        self.token = data["access_token"]

        return data

    def get_incidents(self):
        response = requests.get(
            f"{self.base_url}/incidents/",
            headers=self._headers()
        )

        response.raise_for_status()
        return response.json()

    def create_incident(self, incident):
        response = requests.post(
            f"{self.base_url}/incidents/",
            json=incident,
            headers=self._headers()
        )

        response.raise_for_status()
        return response.json()