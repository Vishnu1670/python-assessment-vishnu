#parent class
class Vehicle:
    def __init__(self,vehicle_number):
        self.vehicle_number = vehicle_number

    #method to calculate the distance_km
    def calculate_fare(self, distance_km):
        pass

#child class
class Bike(Vehicle):
    
    def calculate_fare(self, distance_km):
        base_fare = 20 
        per_km = 8   
        return base_fare + (distance_km*per_km) #20 + (distance_km*8)
    
#child class
class Auto(Vehicle):

    def calculate_fare(self, distance_km):
        base_fare = 30 
        per_km = 12   
        return base_fare + (distance_km*per_km)
    
#child class 
class Car(Vehicle):

    def calculate_fare(self, distance_km):
        base_fare = 50 
        per_km = 18   
        return base_fare + (distance_km*per_km)
    
class Driver:

    def __init__(self,name,licence_no,vehicle):
        self.name = name
        self.licence = licence_no
        self.vehicle = vehicle

class Ride:
    def __init__(self, driver, passenger, pickup, drop, distance):

        self.driver = driver
        self.passenger = passenger
        self.pickup = pickup
        self.drop = drop
        self.distance = distance

    def total_fare(self):

        return self.driver.vehicle.calculate_fare(self.distance)
    
    def driver_earning(self):
        fare = self.total_fare()
        earning = (fare * 80) / 100
        return earning
    
    def summary(self):
            print(f"Passenger: {self.passenger}")

            print(
                f"Driver: {self.driver.name} "
                f"({self.driver.vehicle.__class__.__name__} "
                f"{self.driver.vehicle.vehicle_number})"
            )
            print(
                f"Route: {self.pickup} -> {self.drop} "
                f"({self.distance} km)"
            )
            print(f"Total Fare: Rs.{self.total_fare()}")
            print(f"Driver Earning: Rs.{self.driver_earning()}")



d = Driver(
    "Suresh",
    "DL-9988",
    Car("TN-22-AB-1234")
)

ride = Ride(
    d,
    "Meena",
    "Gandhipuram",
    "Airport",
    15
)

ride.summary()