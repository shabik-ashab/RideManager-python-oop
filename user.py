import hashlib

class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open('users.txt', 'w') as file:
            file.write(f"{email} {pwd_encrypted}")
        file.close()
        print(self.name, 'user created')

    @staticmethod
    def log_in(email, password):
        stored_password = ''
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_password = line.split(' ')[1]
        
        file.close()
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == stored_password:
            print('valid user')
        else:
            print('invalid user')

class Rider(User):
    def __init__(self,name,email,password,location,balance):
        self.location = location
        self.balance = balance
        super().__init__(name,email,password)

    def set_location(self,location):
        self.location = location

    def get_location(self):
        return self.location

    def request_trip(self,destination):
        pass
    
    def start_trip(self,fare):
        self.balance -= fare


hero = User('Hero Alom', "hero@mail.com", '123')

hero.log_in('hero@mail.com', '1234')