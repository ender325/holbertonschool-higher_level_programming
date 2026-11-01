#!/usr/bin/python3
"""Defines an abstract base class Animal and its subclasses Dog and Cat."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Represents an abstract Animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses."""
        pass


class Dog(Animal):
    """Represents a Dog subclass inheriting from Animal."""

    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Represents a Cat subclass inheriting from Animal."""

    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"
