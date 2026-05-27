#!/usr/bin/python3
"""
Module task_00_abc: Defines abstract class Animal and its subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an Animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Class representing a Dog, subclass of Animal.
    """

    def sound(self):
        """
        Returns the sound 'Bark'.
        """
        return "Bark"


class Cat(Animal):
    """
    Class representing a Cat, subclass of Animal.
    """

    def sound(self):
        """
        Returns the sound 'Meow'.
        """
        return "Meow"

