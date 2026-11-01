#!/usr/bin/python3
"""Defines SwimMixin, FlyMixin, and a composite Dragon class."""


class SwimMixin:
    """A mixin that provides swimming capability."""

    def swim(self):
        """Print the creature swimming message."""
        print("The creature swims!")


class FlyMixin:
    """A mixin that provides flying capability."""

    def fly(self):
        """Print the creature flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a Dragon that inherits swimming and flying capabilities via mixins."""

    def roar(self):
        """Print the dragon roaring message."""
        print("The dragon roars!")


if __name__ == "__main__":
    # Instantiate a Dragon object and test its abilities
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
