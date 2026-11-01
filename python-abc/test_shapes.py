#!/usr/bin/env python3
from task_01_duck_typing import Shape, Circle, Rectangle, shape_info
import inspect

# Shape is abstract and exposes both abstract methods
print(Shape.__abstractmethods__)  # expect: frozenset({'area', 'perimeter'})

# Shape can't be instantiated
try:
    Shape()
    print("FAIL: Shape instantiated")
except TypeError:
    print("OK: Shape is abstract")

# Inheritance
print(issubclass(Circle, Shape), issubclass(Rectangle, Shape))

# A subclass missing a method must fail
class Bad(Shape):
    def area(self):
        return 1

try:
    Bad()
    print("FAIL: incomplete subclass instantiated")
except TypeError:
    print("OK: incomplete subclass rejected")

# Duck typing: a class that does NOT inherit from Shape
class Duck:
    def area(self):
        return 1

    def perimeter(self):
        return 2

shape_info(Duck())

# No isinstance in shape_info
print("isinstance" in inspect.getsource(shape_info))  # expect False

# Positional and keyword construction
print(Circle(5).area(), Circle(radius=5).area())
print(Rectangle(4, 7).area(), Rectangle(width=4, height=7).area())
