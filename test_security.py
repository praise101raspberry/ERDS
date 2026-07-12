from app.auth.security import hash_password, verify_password

password = "ERDS123"

hashed = hash_password(password)

print("Password:", password)
print("Hash:", hashed)

print("Correct Password:",
      verify_password("ERDS123", hashed))

print("Wrong Password:",
      verify_password("WrongPassword", hashed))