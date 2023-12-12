from model.dao.AdminDAO import *

class AdminController:
    def authenticate(self, username ,password):
        admin_dao = AdminDao()
        admin_service = admin_dao.check_username_existence(username)
        

        if admin_service != None and username == admin_service.username and password == admin_service.password:
            return True
        
        return False
