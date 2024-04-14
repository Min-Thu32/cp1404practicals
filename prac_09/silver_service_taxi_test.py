from silver_service_taxi import SilverServiceTaxi


# Test the fare calculation for a SilverServiceTaxi
def test_silver_service_taxi_fare():
    silver_taxi = SilverServiceTaxi("Hummer", 200, 2)
    silver_taxi.start_fare()
    silver_taxi.drive(18)
    assert silver_taxi.get_fare() == 48.8  # Rounded to the nearest 10 cents
    print(silver_taxi)


# Run the tests
test_silver_service_taxi_fare()
print("All tests passed!")