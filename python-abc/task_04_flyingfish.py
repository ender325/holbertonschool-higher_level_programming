#!/usr/bin/python3
"""Defines Fish, Bird, and a multiple-inheritance class FlyingFish."""


class Fish:
    """Represents a standard fish."""

    def swim(self):
        """Print the fish swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Print the fish habitat message."""
        print("The fish lives in water")


class Bird:
    """Represents a standard bird."""

    def fly(self):
        """Print the bird flying message."""
        print("The bird is flying")

    def habitat(self):
        """Print the bird habitat message."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish inheriting from both Fish and Bird."""

    def fly(self):
        """Print the flying fish soaring message."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print the flying fish swimming message."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the flying fish habitat message."""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    # Instantiate a FlyingFish and test its methods
    my_flying_fish = FlyingFish()
    my_flying_fish.fly()
    my_flying_fish.swim()
    my_flying_fish.habitat()

    # Investigate the Method Resolution Order (MRO)
    print(FlyingFish.mro())
