from model.dao.AdminDAO import *
import bcrypt

class AdminController:
    def authenticate(self, username ,password):
        admin_dao = AdminDao()
        admin_service = admin_dao.check_username_existence(username)

        # Check that a unhashed password matches one that has previously been hashed
        if  admin_service!= None and bcrypt.checkpw(password.encode('utf-8'), admin_service.password) and username == admin_service.username:
            print("It Matches!") 
            return True
        else:
            print("It Does not Match :(")
        

        
        return False
