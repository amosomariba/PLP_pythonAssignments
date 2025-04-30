class Animal:
    def move(self):
        pass  # This is a base method meant to be overridden

class Bird(Animal):
    def move(self):
        print("Flying through the sky!")

class Fish(Animal):
    def move(self):
        print("Swimming in the water! ")

class Cheetah(Animal):
    def move(self):
        print("Running on land at lightning speed!")

# Example usage
animals = [Bird(), Fish(), Cheetah()]

for animal in animals:
    animal.move()  # Each object responds differently to the same method
