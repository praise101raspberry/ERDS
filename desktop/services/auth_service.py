from services.api_client import APIClient


class AuthService:
    def __init__(self):
        self.api = APIClient()

    def login(self, username, password):
        return self.api.post(
            "/login",
            {
                "username": username,
                "password": password
            }
        )