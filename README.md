# Exercise: Car Management System

*My solution to Code Platoons OOP Car Management exercise*

In this exercise, I was asked to create a Python class called `Car` to manage a collection of cars in a terminal-based application. The goal was to practice using class and instance methods, while also understanding the distinction between them.

## How To Run It

### Requirements:
- Python 3.11 or newer
- *(Optional)* Docker: to run the app or tests without installing Python locally 

### Run The Application Locally
```bash
python3 car_management.py
```
Launches the interactive menu.
Follow the prompts to add cars, view them, see details, record services, and update mileage. 

### Run Tests Locally
```bash
pip install pytest
python3 -m pytest -v
```

### Run The Application In Docker
```bash
docker build -t vehicle-shop .
docker run -it vehicle-shop
```
The `-it` flags are required for the app to work and read the keyboard input. This creates an interactive terminal for the app.

### Run The Test In Docker
```bash
docker build -f Dockerfile.test -t vehicle-shop-tests .
docker run vehicle-shop-tests
```


## Step 0: Class Definition

Create a class named `Car` with the following attributes:

- `all_cars` (class attribute): A list/dictionary that will store all the car instances created.
- `total_cars` (class attribute): An integer that will keep track of the total number of cars.

Implement the constructor `__init__` method to initialize the instance attributes:

- `_id` (instance attribute): An integer that should never be repeated and only rise with each car instance
- `_make` (instance attribute): A string representing the make of the car.
- `_model` (instance attribute): A string representing the model of the car.
- `_year` (instance attribute): An integer representing the manufacturing year of the car.
- `_mileage` (instance attribute): An integer representing the vehicles total mileage
- `_services` (instance attribute): A list that will store the services done to the car.

## Step 1: Terminal Application

Create a terminal application to interact with your Car class. For each option in the menu provided, utilize class and instance attributes and instance methods to run your terminal program as expected. Use Python built in methods such as `input` to allow the user to input data through the terminal.

```bash
----  WELCOME  ----
1. Add a car
2. View all cars
3. View total number of cars
4. See a car's details
5. Service a car
6. Update mileage
7. Quit
```

### Conclusion

This exercise offers hands-on experience in using class and instance methods to create a car management system. You've practiced distinguishing between methods that operate at the class level and those that operate at the instance level. By working on this exercise, you'll reinforce your understanding of these concepts and their practical application in object-oriented programming.

As always, ensure that you follow good coding practices, such as using meaningful variable names, writing clear comments, and maintaining proper indentation. Happy coding!
