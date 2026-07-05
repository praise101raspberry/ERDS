import requests


class APIClient:

    BASE_URL = "http://127.0.0.1:8000"

    def get(self, endpoint):
        response = requests.get(
            f"{self.BASE_URL}{endpoint}"
        )

        response.raise_for_status()

        return response.json()

    def post(self, endpoint, data):
        response = requests.post(
            f"{self.BASE_URL}{endpoint}",
            json=data
        )

        response.raise_for_status()

        return response.json()