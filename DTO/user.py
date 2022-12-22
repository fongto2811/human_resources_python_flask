import bcrypt

class UserDTO:
    def __init__(self, username, password, name, phone, email, address) -> object:
        '''
        Create new User
        '''
        if(not username):
            raise NameError('Username is required.')
        if(type(username) != type(str)):
            raise NameError('Username must be String.')
        if(not password):
            raise NameError('Password is required.')
        if(type(password) != type(str)):
            raise NameError('Password must be String.')
        self.username = username
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        salt = bcrypt.gensalt()
        self.__password = bcrypt.hashpw(password.encode('utf-8'),salt)
        