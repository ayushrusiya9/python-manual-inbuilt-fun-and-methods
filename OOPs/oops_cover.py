# ================== OOPS (Object Oriented Programming) ==================

# OOPS -> a programming approach based on objects and classes.
# It helps to write reusable, scalable, and maintainable code.


# ================== CLASS & OBJECT ==================

# Class -> blueprint/template used to create objects.
# Object -> real instance of a class.

class Student:
    pass

s1 = Student()   # object creation


# ================== SELF KEYWORD ==================

# self -> reference to the current object.
# It is used to access variables and methods of the same object.
# self is NOT a keyword, it is just a convention.

class Demo:
    def show(self):
        print("self refers to:", self)

d = Demo()
d.show()


# ================== CONSTRUCTOR ==================

# Constructor -> special method used to initialize object data.
# __init__ runs automatically when object is created.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Aashu", 21)


# ================== VARIABLES IN CLASS ==================

# Instance variable -> belongs to object (different for each object)
# Class variable -> shared by all objects

class College:
    college_name = "RGPV"     # class variable

    def __init__(self, name):
        self.name = name      # instance variable


# ================== TYPES OF METHODS ==================

class MathOps:

    def instance_method(self):
        return "uses self (object)"

    @classmethod
    def class_method(cls):
        return "uses cls (class)"

    @staticmethod
    def static_method(a, b):
        return a + b


# ================== 4 PILLARS OF OOPS ==================

# ------------------------------------------------------
# 1. ENCAPSULATION
# ------------------------------------------------------

# Encapsulation -> wrapping data (variables) and methods inside a class.
# It helps to protect data and control access.

# Access modifiers (Python uses conventions):

# Public -> accessible everywhere
# Protected -> single underscore (_), meant for child classes
# Private -> double underscore (__), uses name mangling

class A:
    def __init__(self):
        self.x = 10        # public
        self._y = 20       # protected
        self.__z = 30      # private

    def __xyz(self):
        return "private method"

# Name mangling format:
# _ClassName__privateName


# ------------------------------------------------------
# 2. ABSTRACTION
# ------------------------------------------------------

# Abstraction -> hiding implementation details and showing only required features.
# Implemented using abstract classes.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Bike(Vehicle):
    def start(self):
        print("Bike starts")

# Vehicle() not allowed
# Bike() allowed


# ------------------------------------------------------
# 3. INHERITANCE
# ------------------------------------------------------

# Inheritance -> acquiring properties and methods from parent class.

class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    pass

c = Child()
c.show()

# Types of inheritance:
# - Single
# - Multilevel
# - Multiple
# - Hierarchical

# Python supports multiple inheritance.


# ------------------------------------------------------
# 4. POLYMORPHISM
# ------------------------------------------------------

# Polymorphism -> same method name, different behavior.
# Python supports method overriding and duck typing.

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()


# ================== METHOD OVERRIDING ==================

# Child class provides its own implementation of parent method.

class Base:
    def show(self):
        print("Base class")

class Derived(Base):
    def show(self):
        print("Derived class")


# ================== SUPER KEYWORD ==================

# super() -> used to call parent class methods or constructor.

class P:
    def __init__(self):
        print("Parent init")

class C(P):
    def __init__(self):
        super().__init__()
        print("Child init")


# ================== IS-A vs HAS-A ==================

# IS-A -> inheritance
# HAS-A -> composition (object inside another object)

class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()   # HAS-A relationship


# ================== NAME MANGLING ==================

# Name mangling -> Python internally changes private names
# Format:
# _ClassName__privateVariableOrMethod

# This avoids accidental access and method overriding.

# ================== PRACTICAL EXAMPLE ==================

class A:
    def __init__(self):
        self.__x = 10

    def __xyz(self):
        return "Private method from class A"

    def show(self):
        return self.__xyz()


class C(A):
    pass


obj = C()

# Direct access  (will give error)
# obj.__xyz()

# Correct access using name mangling
print(obj._A__xyz())

# ================== INTERFACE (Python style) ==================

# Python does not have interface keyword.
# Abstract class with only abstract methods works as interface.


# ================== IMPORTANT INTERVIEW FACTS ==================

# Python is object-oriented but not 100% pure OOP
# Everything in Python is an object
# No strict access modifiers (public/protected/private are conventions)
# Multiple inheritance supported
# Method overloading is NOT supported (last definition wins)
# method overrding is supported
