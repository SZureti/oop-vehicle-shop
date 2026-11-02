import pytest
from car_management import Car

@pytest.fixture(autouse=True)
def reset_car_state():
    # Reset the class attributes before each test
    Car.all_cars = []
    Car.total_cars = 0
    yield

# Make sure that the year is a 4 digit number.
def test_year_is_four_digits():
    car = Car(make="Toyota", model="Camry", year=2020, color="Blue", mileage=15000)
    assert len(str(car._year)) == 4

def test_invalid_year_raises_error():
    # A year that is not a 4-digit number should be rejected
    with pytest.raises(ValueError):
        Car(make="Honda", model="Civic", year=21, color="Red", mileage=10000)

def test_car_id_is_unique_and_rising():
    car1 = Car(make="Ford", model="Mustang", year=2019, color="Black", mileage=20000)
    car2 = Car(make="Chevrolet", model="Camaro", year=2020, color="Yellow", mileage=15000)
    car3 = Car(make="Dodge", model="Challenger", year=2021, color="Blue", mileage=5000)
    assert car1._id == 1
    assert car2._id == 2
    assert car3._id == 3
    assert car1._id != car2._id
    assert car2._id != car3._id
    assert car3._id != car1._id

def test_car_is_created_with_correct_attributes():
    car = Car(make="Toyota", model="Camry", year=2020, color="Blue", mileage=15000)
    
    assert car._make == "Toyota"
    assert car._model == "Camry"
    assert car._year == 2020
    assert car._color == "Blue"
    assert car._mileage == 15000
    assert car._services == []
    assert car._id == 1

def test_all_cars_collects_each_instance():
    car1 = Car(make="Nissan", model="Altima", year=2018, color="White", mileage=30000)
    car2 = Car(make="BMW", model="3 Series", year=2021, color="Silver", mileage=5000)
    car3 = Car(make="Audi", model="A4", year=2022, color="Gray", mileage=1000)
    assert len(Car.all_cars) == 3
    assert car1 in Car.all_cars
    assert car2 in Car.all_cars
    assert car3 in Car.all_cars

def test_services_start_empty_and_are_independent():
    car1 = Car(make="Audi", model="A4", year=2022, color="Gray", mileage=1000)
    car2 = Car(make="Mercedes-Benz", model="C-Class", year=2021, color="Black", mileage=2000)
    car3 = Car(make="Volkswagen", model="Golf", year=2020, color="Blue", mileage=15000)
    
    assert car1._services == []
    assert car2._services == []
    assert car3._services == []
    
    # Add a service to car1
    car1.add_service("Oil Change")

    # Add a service to car2
    car2.add_service("Brake Inspection")
    
    assert car1._services == ["Oil Change"]
    assert car2._services == ["Brake Inspection"]  # Make sure car2's services remain unaffected 
    assert car3._services == []  # Make sure car3's services remain unaffected

def test_add_service_appends():
    car = Car(make="Tesla", model="Model 3", year=2021, color="Red", mileage=5000)
    
    # Add a service
    car.add_service("Tire Rotation")
    assert car._services == ["Tire Rotation"]

def test_update_mileage_changes_value():
    car = Car(make="Subaru", model="Outback", year=2020, color="Green", mileage=10000)
    
    # Update mileage
    car.update_mileage(12000)
    assert car._mileage == 12000
