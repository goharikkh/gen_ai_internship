#The task involves implementing descriptor classes in
# Python to enforce type validation for attributes in a
# Person class. The goal is to ensure that the assigned values
# for specific attributes have the correct types and raise a
# ValueError if an incorrect type is provided.


class ValidType:
    def __init__(self, data_type):
        self.data_type = data_type

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, self.data_type):
            raise ValueError(
                f"Invalid type for attribute '{self.name}'. Expected {self.data_type.__name__}, but got {type(value).__name__}."
            )
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Person:
    age = ValidType(int)
    height = ValidType(float)
    tags = ValidType(list)
    favorite_foods = ValidType(tuple)
    name = ValidType(str)

    def __init__(self, age, height, tags, favorite_foods, name):
        self.age = age
        self.height = height
        self.tags = tags
        self.favorite_foods = favorite_foods
        self.name = name



# Example 1: Correct input types
person1 = Person(25, 175.5, ["friendly", "smart"], ("pizza", "sushi"), "John Doe")

# Example 2: Incorrect input types
try:
    person3 = Person(25, "175.5", ["friendly", "smart"], ("pizza", "sushi"), "John Doe")
except ValueError as e:
    print(e)



