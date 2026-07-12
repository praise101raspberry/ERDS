from app.database.database import SessionLocal
from app.models.user import User

db = SessionLocal()

user = db.query(User).filter(User.username == "admin").first()

if user:
    db.delete(user)
    db.commit()
    print("Admin user deleted.")
else:
    print("Admin user not found.")

db.close()