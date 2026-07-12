from app.auth.jwt_handler import (
    create_access_token,
    verify_access_token,
)

token = create_access_token(
    {"sub": "admin"}
)

print("Token:")
print(token)

print()

print("Decoded:")
print(
    verify_access_token(token)
)