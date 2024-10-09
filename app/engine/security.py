from werkzeug.security import generate_password_hash, check_password_hash
from app.models import MasterUser
from app import db, app

class Admin():
    def __init__(self):
        with app.app_context():
            MasterUser.set_initial_admin()
            master_user = MasterUser.get_master_user()
            self.__user = master_user.username
            self.__pw_hash = master_user.password

    def check_password(self, password):
        return check_password_hash(self.__pw_hash, password)
    

    def check_username(self, username):
        return self.__user == username

    def update_credentials(self, new_username, new_password):
        with app.app_context():
            master_user = MasterUser.get_master_user()
            master_user.username = new_username
            master_user.password = generate_password_hash(new_password)
            db.session.commit()
            self.__user = new_username
            self.__pw_hash = master_user.password

