from services.api_client import APIClient


class IncidentService:

    def __init__(self):
        self.api = APIClient()

    def get_incidents(self):
        return self.api.get("/incidents")