
class RideManager:
    def __init__(self) -> None:
        print("ride manager activated")
        self.__avilable_cars = []
        self.__avilable_bikes = []
        self.__avilable_cng = []

    def add_vehicle(self, vehicle_type, vehicle):
        if vehicle_type == 'car':
            self.__avilable_cars.append(vehicle)
        if vehicle_type == 'bike':
            self.__avilable_bikes.append(vehicle)
        else:
            self.__avilable_cng.append(vehicle)

    def get_avilable_cars(self):
        return self.__avilable_cars

    def find_veichle(self,rider,vehicle_type,destination):
        if vehicle_type == 'car':
            if(len(self.__avilable_cars) == 0):
                print('No cars avilable')
                return False
            for car in self.__avilable_cars:
                print(rider.location, car.owner.location)
                if abs(rider.location - car.owner.location) < 30:
                    print('find a match')


uber = RideManager()
