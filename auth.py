import getpass

class Auth:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def init(self):
        if not self.username:
            self.username = input("Username?\n> ")
        if not self.password:
            self.password = getpass.getpass("Password?\n> ")
    
    def get_tuple(self):
        return self.username, self.password
