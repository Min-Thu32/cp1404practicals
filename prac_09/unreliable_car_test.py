from unreliable_car import UnreliableCar

# Create an UnreliableCar object with name "Unreliable Car", 100 units of fuel, and reliability of 50%
my_car = UnreliableCar("Unreliable Car", 100, 50)

# Test-driving the car for 10 km
distance_driven = my_car.drive(10)
print("Distance driven:", distance_driven)

# Test-driving the car for 20 km
distance_driven = my_car.drive(20)
print("Distance driven:", distance_driven)
