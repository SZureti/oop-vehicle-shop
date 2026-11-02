class Car:
    """A class to manage the collection of cars."""
    all_cars = []
    total_cars = 0

    def __init__(self, make, model, year, color, mileage, services=None):
        
        # I added a check so that the year is a 4 digit number.
        if not isinstance(year, int) or len(str(year)) != 4:
            raise ValueError("Year must be a 4-digit integer.")

        # Make the class generate the id automatically and ensure that it is unique and rising with each new instance. Also it prevents the creation of a car with a duplicate id, which could happen if passed as a parameter. 

        self._id = Car.total_cars + 1
        self._make = make
        self._model = model
        self._year = year
        self._color = color
        self._mileage = mileage
        self._services = services if services is not None else []

        # Add the new car instance to the class attributes
        Car.all_cars.append(self)
        Car.total_cars += 1

    def add_service(self, service):
        """Record a service performed on this car."""
        self._services.append(service)

    def update_mileage(self, new_mileage):
        """Update the mileage of the car. The new mileage must be greater than or equal to the current mileage."""
        if new_mileage < self._mileage:
            raise ValueError("New mileage cannot be less than current mileage.")
        self._mileage = new_mileage

    def __str__(self):
        return f"Car(id={self._id}, make={self._make}, model={self._model}, year={self._year}, color={self._color}, mileage={self._mileage})"

    # Class methods to add a new car, view all cars, and find a car by its ID. 
    @classmethod
    def add_car(cls):
        """Prompt the user for car details and create a new Car instance."""
        make = input("Make: ")
        model = input("Model: ")
        year = int(input("Year: "))
        color = input("Color: ")
        mileage = int(input("Mileage: "))
        services = []
        if input("Add a service? (y/n): ").lower() == "y":
            services = input("Service performed: ").split(",")
        
        return cls(make, model, year, color, mileage, services)

    @classmethod
    def view_all(cls):
        """Print all cars in the collection."""
        if not cls.all_cars:
            print("No cars available.")
        for car in cls.all_cars:
            print(car)

    @classmethod
    def find_by_id(cls, car_id):
        """Find a car by its ID."""
        for car in cls.all_cars:
            if car._id == car_id:
                return car
        return None

# Create Menu 

if __name__ == "__main__":
    while True:
        print("""
----  WELCOME  ----
1. Add a car
2. View all cars
3. View total number of cars
4. See a car's details
5. Service a car
6. Update mileage
7. Quit
""")
        choice = input("Select an option: ")

        if choice == "1":
            Car.add_car()
            print("Car added!")

        elif choice == "2":
            Car.view_all()

        elif choice == "3":
            print(f"Total cars: {Car.total_cars}")

        elif choice == "4":
            car_id = int(input("Enter car id: "))
            car = Car.find_by_id(car_id)
            if car:
                print(car)
                print(f"Services: {car._services}")
            else:
                print("No car with that id.")

        elif choice == "5":
            car_id = int(input("Enter car id: "))
            car = Car.find_by_id(car_id)
            if car:
                car.add_service(input("Service performed: "))
                print("Service recorded.")
            else:
                print("No car with that id.")

        elif choice == "6":
            car_id = int(input("Enter car id: "))
            car = Car.find_by_id(car_id)
            if car:
                try:
                    car.update_mileage(int(input("New mileage: ")))
                    print("Mileage updated.")
                except ValueError as e:
                    print(e)          # e.g. "New mileage cannot be less than current"
            else:
                print("No car with that id.")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option, please choose 1-7.")
