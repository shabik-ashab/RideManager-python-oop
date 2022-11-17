import hashlib
from random import randint, choice
import threading

from brta import BRTA
from vehicle import Car, Cng, Bike
from ride_manager import uber

license_authority = BRTA()

class UserAlreadyExist(Exception):
    def __init__(self,email, *args: object) -> None:
        print(f'User: {email} already exists.')
        super().__init__(*args)


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.__trip_history = []
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        already_exist = False
        with open ('users.txt', 'r') as file:
            if email in file.read():
                already_exist = True
                # raise UserAlreadyExist(email)
        file.close()

        if already_exist == False:
            with open('users.txt', 'a') as file:
                file.write(f"{email} {pwd_encrypted}\n")
            file.close()

        # print(self.name, 'user created')

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
        self.__trip_history = []
        super().__init__(name, email, password)

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def request_trip(self, destination):
        pass

    def get_trip_history(self):
        return self.__trip_history

    def start_trip(self, fare, trip_info):
        print(f"trip started for {self.name}")
        self.balance -= fare
        self.__trip_history.append(trip_info)


class Driver(User):
    def __init__(self, name, email, password, location, license):
        super().__init__(name, email, password)
        self.location = location
        self.license = license
        self.__trip_history = []
        self.valid_driver = license_authority.validate_licence(email, license)
        self.earning = 0
        self.vehicle = None

    def take_driving_test(self):
        res = license_authority.driving_test(self.email)
        if res:
            self.license = res
            self.valid_driver = True

    def register_vehicle(self, vehicle_type, licence_plate, rate):
        if self.valid_driver:
            if vehicle_type == 'car':
                self.vehicle = Car(
                    vehicle_type, licence_plate, rate, self)
                uber.add_vehicle(vehicle_type,self.vehicle)
            elif vehicle_type == 'bike':
                self.vehicle = Bike(
                    vehicle_type, licence_plate, rate, self)
                uber.add_vehicle(vehicle_type, self.vehicle)
            else:
                self.vehicle = Cng(
                    vehicle_type, licence_plate, rate, self)
                uber.add_vehicle(vehicle_type,self.vehicle)
        else:
            # print("invalid driver")
            pass


    def get_trip_history(self):
        return self.__trip_history

    def start_trip(self,start, destination, fare, trip_info):
        self.earning += fare
        self.location = destination
        # start a thrad
        trip_thread = threading.Thread(target=self.vehicle.start_driving, args=(start,destination))
        trip_thread.start()
        # self.vehicle.start_driving(start, destination)
        self.__trip_history.append(trip_info)


vehicle_types = ['bike','cng','car']


rider1 = Rider('rider1', 'rider@mail.com', 'rider1', randint(0,60), 4000)
rider2 = Rider('rider2', 'rider2@mail.com', 'rider2', randint(0,60), 4000)
rider3 = Rider('rider3', 'ride3@mail.com', 'rider3', randint(0,60), 4000)

for i in range(1,100):
    driver1 = Driver(f'd{i}', f'd{i}@mail.com', f'd{i}', randint(0,60),randint(5555,9999))
    driver1.take_driving_test()
    driver1.register_vehicle(choice(vehicle_types), randint(11111,99999), randint(10,20))

# driver1 = Driver('d1', 'd1@mail.com', 'd1', randint(0,60),3445)
# driver1.take_driving_test()
# driver1.register_vehicle('car', 1245, 10)

print(len(uber.get_avilable_cars()))
uber.find_veichle(rider1,choice(vehicle_types), randint(1,100))
uber.find_veichle(rider2,choice(vehicle_types), randint(1,100))
uber.find_veichle(rider3,choice(vehicle_types), randint(1,100))
# uber.find_veichle(rider1,'car', randint(1,100))
# uber.find_veichle(rider1,'car', randint(1,100))

print(rider1.get_trip_history())
print(uber.total_income())
