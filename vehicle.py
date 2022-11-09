from abc import ABC, abstractmethod

class Vehicle:
    speed = {
        'car': 30,
        'bike': 50,
        'cng': 15
    }
    def __init__(self, vechile_type,licence_plate,rate,owner) -> None:
        self.vechile_type = vechile_type
        self.rate = rate
        self.driver = owner
        self.licence_plate = licence_plate
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

    def start_driving(self):
        print(self.vechile_type,self.licence_plate,'started')

    def trip_finished(self):
        print(self.vechile_type,self.licence_plate,'complete trip')


class Bike(Vehicle):
    def __init__(self, vechile_type, licence_plate, rate, owner) -> None:
        super().__init__(vechile_type, licence_plate, rate, owner)

    def start_driving(self):
        print(self.vechile_type,self.licence_plate,'started')

    def trip_finished(self):
        print(self.vechile_type,self.licence_plate,'complete trip')


class Cng(Vehicle):
    def __init__(self, vechile_type, licence_plate, rate, owner) -> None:
        super().__init__(vechile_type, licence_plate, rate, owner)

    def start_driving(self):
        print(self.vechile_type,self.licence_plate,'started')

    def trip_finished(self):
        print(self.vechile_type,self.licence_plate,'complete trip')