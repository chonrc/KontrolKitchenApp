from model.entities.Client import Client

class ClientDTO(Client):
    def __init__(self, username, user_id):
        super().__init__(username, None, user_id)
        
       

    def get_username(self):
        return self.username

    def get_id(self):
        return self.id
