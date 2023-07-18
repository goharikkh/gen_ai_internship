# Implement a hierarchy of classes representing different types of vehicles, such as cars, motorcycles, and bicycles.
# Demonstrate inheritance, method overriding, and polymorphism by implementing common methods
# and attributes specific to each vehicle type.
from abc import ABC


class Vehicle(ABC):
    def __init__(self, model, year, color, owner=None):
        self._model = model
        self._color = color
        self._year = year
        self._owner = owner

    @property
    def model(self):
        return self._model

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def year(self):
        return self._year

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        self._owner = new_owner


class Car(Vehicle):
    def __init__(self, model, year, color, owner=None):
        super().__init__(model, year, color, owner)

    def drive(self):
        print(f"Driving {self._model}")

    def get_info(self):
        print(f"Car {self._model} is {self._color} and was built in {self._year}")


class Motorcycle(Vehicle):
    def __init__(self, model, year, color):
        super().__init__(model, year, color)

    def get_info(self):
        return f"{self.year} {self.model}"

    def drive(self):
        print(f"Driving {self._model}")


class Truck(Vehicle):
    def __init__(self, model, year, color, max_load):
        super().__init__(model, year, color)
        self._max_load = max_load

    def drive(self):
        print(f"Driving {self._model} with max load {self._max_load} kg")

    def get_info(self):
        print(f"Truck {self._model} is {self._color} and was built in {self._year}")


class Bicycle(Vehicle):
    def __init__(self, model, year,color):
        super().__init__(model, year, color)

    def get_info(self):
        return f"{self.year} {self.model})"

    def ride(self):
        print(f"{self._model} is now being ridden.")