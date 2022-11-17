
class RideManager:
    def __init__(self) -> None:
        print("ride manager activated")
        self.__income = 0
        self.__avilable_cars = []
        self.__trip_history = []
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
                if abs(rider.location - car.owner.location) < 30:
                    distance = abs(rider.location - destination)
                    fare = distance * car.rate

                    if rider.balance < fare:
                        print('you do not have enough money')
                        return False

                    if car.status == 'avilable':
                        car.status = 'unavilable'
                        self.__avilable_cars.remove(car) 

                        rider.start_trip(destination, fare)
                        car.owner.start_trip(destination, fare*0.8)

                        self.__income += fare*0.20
                        print(rider.location, car.owner.location, ' -> ', destination)
                        
                        trip_info = f"find a match for {rider.name} for fare: {fare} with {car.owner.name} started: {rider.location} to: {destination}"
                        self.__trip_history.append(trip_info)
                        print(trip_info)
                        return True 


uber = RideManager()
