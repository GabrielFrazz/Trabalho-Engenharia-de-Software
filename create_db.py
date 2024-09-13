from app import db, app
from app.models import Cliente, Produto  

with app.app_context():
    db.create_all()