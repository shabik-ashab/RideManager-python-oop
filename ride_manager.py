
class RideManager:
    def __init__(self) -> None:
        print("ride manager activated")
        self.__avilable_cars = []
        self.__avilable_bikes = []
        self.__avilable_cng = []

    def add_veichle(self,vehicle_type,vehicle):
        if vehicle_type == 'car':
            self.__avilable_cars.append(vehicle)
        if vehicle_type == 'bike':
            self.__avilable_bike.append(vehicle)
        else:
            self.__avilable_cng.append(vehicle)

    def match_veichle(self):
        pass

uber = RideManager()