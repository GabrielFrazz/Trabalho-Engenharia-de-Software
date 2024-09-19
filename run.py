from app import app
from app.engine.security import Admin

# Ensure the database is initialized before creating the Admin instance
with app.app_context():
    admin = Admin()

if __name__ == "__main__":
    app.run(debug=True)
