from app import db, app
from app.models import *

with app.app_context():
    db.create_all()
    MasterUser.set_initial_admin()
    print("Database tables created and initial admin set.")