#!/usr/bin/python3
from task_00_abc import Animal, Dog, Cat

def main():
    try:
        bobby = Dog()
        garfield = Cat()

        print(bobby.sound())
        print(garfield.sound())

        print("Attempting to create an Animal instance...")
        animal = Animal()
        print(animal.sound())

    except TypeError as e:
        print(e)

if __name__ == "__main__":
    main()
