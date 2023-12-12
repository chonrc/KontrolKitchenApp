from model.entities.Admin import *
import bcrypt
class AdminService(Admin):
    def __init__(self, username, password):
        # Declaring Password
        password = password.encode('utf-8')

        # Hash a password for the first time, with a randomly-generated salt
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())


        super().__init__(username, hashed, user_id=None) 
