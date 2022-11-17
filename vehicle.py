from abc import ABC, abstractmethod
from time import sleep

class Vehicle:
    speed = {
        'car': 30,
        'bike': 50,
        'cng': 15
    }
    def __init__(self, vechile_type,licence_plate,rate,owner) -> None:
        self.vechile_type = vechile_type
        self.rate = rate
        self.owner = owner
        self.licence_plate = licence_plate
        self.status = 'avilable'
        self.speed = self.speed[vechile_type]

    @abstractmethod
    def start_driving(self):
        pass

    @abstractmethod
    def trip_finished(self):
        pass
    

class Car(Vehicle):
    def __init__(self, vechile_type, licence_plate, rate, owner) -> None:
        super().__init__(vechile_type, licence_plate, rate, owner)

    def start_driving(self, start, destination):
        self.status = 'unavilable'
        print(self.vechile_type,self.licence_plate,'started')
        distance = abs(start - destination)
        for i in range(0,distance):
            sleep(0.5)
            print(f"Driving: {self.licence_plate} curr position: {i} of {distance} \n")
        self.trip_finished()

    def trip_finished(self):
        self.status = 'avilable'
        print(self.vechile_type,self.licence_plate,'complete trip')


class Bike(Vehicle):
    def __init__(self, vechile_type, licence_plate, rate, owner) -> None:
        super().__init__(vechile_type, licence_plate, rate, owner)

    def start_driving(self, start, destination):
        self.status = 'unavilable'
        print(self.vechile_type,self.licence_plate,'started')
        distance = abs(start - destination)
        for i in range(0,distance):
            sleep(0.5)
            print(f"Driving: {self.licence_plate} curr position: {i} of {distance} \n")
        self.trip_finished()

    def trip_finished(self):
        self.status = 'avilable'
        print(self.vechile_type,self.licence_plate,'complete trip')


class Cng(Vehicle):
    def __init__(self, vechile_type, licence_plate, rate, owner) -> None:
        super().__init__(vechile_type, licence_plate, rate, owner)

    def start_driving(self, start, destination):
        self.status = 'unavilable'
        print(self.vechile_type,self.licence_plate,'started')
        distance = abs(start - destination)
        for i in range(0, distance):
            sleep(0.5)
            print(f"Driving: {self.licence_plate} curr position: {i} of {distance} \n")
        self.trip_finished()

    def trip_finished(self):
        self.status = 'avilable'
        print(self.vechile_type,self.licence_plate,'complete trip')