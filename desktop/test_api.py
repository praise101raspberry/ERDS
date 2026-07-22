from services.api_client import APIClient

api = APIClient()

try:
    # If login is required
    # api.login("admin", "your_password")

    result = api.update_incident(
        1,
        {
            "caller_name": "Thoriso Praise",
            "caller_phone": "0821234567",
            "priority": "Critical",
            "status": "Assigned",
            "address": "Pretoria",
            "description": "Updated from APIClient test"
        }
    )

    print("Success!")
    print(result)

except Exception as e:
    print("Error:")
    print(e)