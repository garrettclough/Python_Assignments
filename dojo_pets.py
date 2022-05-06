from mimetypes import init

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
    def sleep(self):
        print("Pet is sleeping.")
        self.energy += 25
        return self
    def eat(self):
        print("Pet is eating.")
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        print("Pet is playing.")
        self.health += 5
        return self
    def noise(self):
        print("Bark!")
        return self

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.irst_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    def walk(self):
        print("Walking the pet.")
        self.pet.play()
        return self
    def feed(self):
        print("Feeding the pet.")
        self.pet.eat()
        return self
    def bathe(self):
        print("Cleaning the pet")
        return self

nibbles = Pet("Mr. Nibbles","Horse",'nibbles on things')
tod = Ninja('Todd', 'Last', 'biscuit', 'kibble', nibbles)

tod.feed()
tod.bathe()