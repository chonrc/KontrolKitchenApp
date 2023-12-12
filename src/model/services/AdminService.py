from model.entities.Admin import *

class AdminService(Admin):
    def __init__(self, username, password):
        super().__init__(username, password, user_id=None) 