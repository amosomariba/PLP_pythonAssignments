# Base class
class Character:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def introduce(self):
        print(f"My name is {self.name}, and I'm from {self.origin}.")

# Subclass
class Superhero(Character):
    def __init__(self, name, origin, power, weakness):
        super().__init__(name, origin)  # Call the constructor of Character
        self.power = power
        self.weakness = weakness

    def use_power(self):
        print(f"{self.name} uses their power: {self.power}!")

    def show_weakness(self):
        print(f"{self.name}'s weakness is {self.weakness}.")

# Example usage
hero1 = Superhero("Photon Blaze", "Neon City", "Laser Vision", "Kryptonite")
hero1.introduce()
hero1.use_power()
hero1.show_weakness()
