"""Dedicnost"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Employee(Person):
    def __init__(self, name, age, rate, num_of_hours):
        super().__init__(name, age)
        self.rate = rate
        self.num_of_hours = num_of_hours

    def show_finance(self):
        return self.rate * self.num_of_hours


class Student(Person):
    def __init__(self, name, age, scholarship):
        super().__init__(name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship


"""vytvoreni studenta a employee"""

if __name__ == "__main__":
    student1 = Student('John', 22, 700)
    employee1 = Employee('Peter', 42, 15, 160)
    print("Dedicnost")
    print(student1)
    print(employee1)
    print(student1.show_finance())
    print(employee1.show_finance())
    print([student1, employee1])
    print(repr(student1))
    print(employee1.__str__() == str(employee1))
    print(student1.__str__())

"""Vicenasobna dedicnost"""

print("Vicenasobna dedicnost")


class Employee(Person):
    def __init__(self, name, age, rate, num_of_hour):
        Person.__init__(self, name, age)
        self.rate = rate
        self.num_of_hour = num_of_hour

    def show_finance(self):
        return self.rate * self.num_of_hour


class Student(Person):
    def __init__(self, name, age, scholarship):
        Person.__init__(self, name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship


class WorkingStudent(Employee, Student):
    """muzu zadat za sebe dedicnost pro vice trid naraz
    lepsi pouzivat pr mixin nez pro dijamant"""

    def __init__(self, name, age, rate, num_of_hour, scholarship):
        Employee.__init__(self, name, age, rate, num_of_hour)
        Student.__init__(self, name, age, scholarship)
        super().__init__(name, age, rate, num_of_hour)

    def show_finance(self):
        return self.rate * self.num_of_hour + self.scholarship


os1 = Person("John", 54)
os2 = Employee("Jack", 36, 20, 160)
os3 = Student("Agatha", 22, 1000)
os4 = WorkingStudent("Monica", 24, 9.5, 70, 550)
print(os1)
print(os2)
print(os3)
print(os4)

"""Polymorfismus je princip OOP, který umožňuje používat společné rozhraní (např. stejné názvy metod) pro 
různé typy objektů."""


def check_finance(obj):
    print(obj.show_finance())


check_finance(os2)  # an instance of the Employee class
check_finance(os3)  # an instance of the Student class

"""Abstraktní třída je zobecněním jiných tříd, ale sama o sobě neexistuje (nelze vytvářet objekty tohoto typu). 
Například třídy jako Kruh, Čtverec a Trojúhelník odpovídají skutečným geometrickým útvarům a každá z nich 
má specifické vlastnosti. Můžeme je však všechny zobecnit na třídu Utvar, která ale přímo neexistuje a 
nemá ani žádné objekty - bude to tedy abstraktní třída s metodami, které jsou společné všem těmto útvárům."""

"""K vytvoření abstraktních tříd použijeme balíček abc. Abstraktní metody nemají tělo a musí být 
implementovány dědičnými metodami."""

from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):
    @abstractmethod
    def circuit(self):
        pass

    @abstractmethod
    def area(self):
        pass


"""Třídy rozšiřující třídu Utvar."""


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def circuit(self):
        return 2 * self.r * pi

    def area(self):
        return pi * self.r ** 2


"""volani"""

rectangle = Rectangle(3, 5)
circle = Circle(12)
print(rectangle.circuit())
print(circle.circuit())
