import hashlib

from brta import BRTA
from vehicle import Car, Cng, Bike
from ride_manager import uber

license_authority = BRTA()


class User:
    def __init__(self, name, email, password):
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
    def __init__(self, name, email, password, location, balance):
        self.location = location
        self.balance = balance
        super().__init__(name, email, password)

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def request_trip(self, destination):
        pass

    def start_trip(self, fare):
        self.balance -= fare


class Driver(User):
    def __init__(self, name, email, password, location, license):
        super().__init__(name, email, password)
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_licence(email, license)
        self.earning = 0

    def take_driving_test(self):
        res = license_authority.driving_test(self.email)
        if res:
            self.license = res
            self.valid_driver = True

    def register_vehicle(self, vehicle_type, licence_plate, rate):
        if self.valid_driver:
            if vehicle_type == 'car':
                new_vehicle = Car(
                    vehicle_type, licence_plate, rate, self.email)
                uber.add_vehicle(vehicle_type,new_vehicle)
            elif vehicle_type == 'bike':
                new_vehicle = Bike(
                    vehicle_type, licence_plate, rate, self.email)
                uber.add_vehicle(vehicle_type, new_vehicle)
            else:
                new_vehicle = Cng(
                    vehicle_type, licence_plate, rate, self.email)
                uber.add_vehicle(vehicle_type,new_vehicle)
        else:
            print("invalid driver")

    def start_trip(self, destination, fare):
        self.earning += fare
        self.location = destination


rider1 = Rider('rider1', 'rider@mail.com', 'rider1', 55, 4000)

driver1 = Driver('d1', 'd1@mail.com', 'd1', 44,3445)
driver1.take_driving_test()

driver1.register_vehicle('car', 1245, 10)

driver2 = Driver('d2', 'd2@mail.com', 'd2', 43,3445)

driver2.take_driving_test()
print(uber.get_avilable_cars())