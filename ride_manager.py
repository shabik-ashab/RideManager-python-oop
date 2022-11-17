
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

    def total_income(self):
        return self.__income
    
    def trip_history(self):
        return self.__trip_history

    def find_veichle(self,rider,vehicle_type,destination):
        if vehicle_type == 'car':
            vehicles = self.__avilable_cars
        elif vehicle_type == 'bike':
            vehicles = self.__avilable_bikes
        else:
            vehicles = self.__avilable_cng 

        if(len(vehicles) == 0):
            print('No cars avilable')
            return False
            
        for vehicle in vehicles:
            if abs(rider.location - vehicle.owner.location) < 30:
                distance = abs(rider.location - destination)
                fare = distance * vehicle.rate

                if rider.balance < fare:
                    print('you do not have enough money')
                    return False

                if vehicle.status == 'avilable':
                    vehicle.status = 'unavilable'
                    vehicles.remove(vehicle) 

                    trip_info = f"Match {vehicle_type} for {rider.name} for fare: {fare} with {vehicle.owner.name} started: {rider.location} to: {destination}"
                    print(trip_info)
                    rider.start_trip(fare, trip_info)
                    vehicle.owner.start_trip(rider.location,destination, fare*0.8, trip_info)

                    self.__income += fare*0.20
                    print(rider.location, vehicle.owner.location, ' -> ', destination)
                    
                    self.__trip_history.append(trip_info)
                    return True 


uber = RideManager()
