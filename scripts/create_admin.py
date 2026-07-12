from app.database.database import SessionLocal
from app.models.user import User
from app.auth.security import hash_password

db = SessionLocal()

# Check if admin already exists
existing = db.query(User).filter(User.username == "admin").first()

if existing:
    print("Admin user already exists.")
else:
    admin = User(
        username="admin",
        email="admin@erds.local",
        hashed_password=hash_password("Admin123!")
    )

    db.add(admin)
    db.commit()

    print("Admin user created successfully!")

db.close()