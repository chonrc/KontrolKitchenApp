from model.entities.Admin import *
import bcrypt
class AdminDTO(Admin):
    def __init__(self, username, password):
        super().__init__(username, password, None)
        
       

    def get_username(self):
        return self.username

    def get_pass(self):
        return self.password