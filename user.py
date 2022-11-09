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


hero = User('Hero Alom', "hero@mail.com", '123')