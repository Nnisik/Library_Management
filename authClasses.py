import db
from authClasses import LoginGUI

class Login:
    def loginUser(self, login, password):
        self.login = login
        self.password = password

    def checkUserExist(self):
        if db.checkUserExist(self.login):
            return True
        else:
            print("Login not exist")
            return False

class Signup:
    def signupUser(self, login, password, password_rpt):
        self.login = login
        self.password = password
        self.password_rpt = password_rpt

        if not self.checkUserNotExist():
            print('user with this name is alredy registered')
            exit()
        
        if self.passwordsMatch():
            print("Password and password repeat don't match")
            exit()
        
        db.addNewUser(self)
    
    def checkUserNotExist(self):
        if db.checkUserExist(self.login):
            print("This user already exists!")
            return False
    
    def passwordsMatch(self):
        return not self.password == self.password_rpt