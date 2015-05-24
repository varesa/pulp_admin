import getpass

class Auth():
    def __init__(self):
        self.username = ""
        self.password = ""

    def init(self):
        self.username = input("Username?\n> ")
        self.password = getpass.getpass("Password?\n> ")
    
    def get_tuple(self):
        return self.username, self.password