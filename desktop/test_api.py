from services.api_client import APIClient

api = APIClient()

incidents = api.get_incidents()

print(incidents)