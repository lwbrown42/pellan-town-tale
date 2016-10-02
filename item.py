import random
import character

class Item:

    def __init__(self, name, description, min_dam, max_dam, armor):
        self.name = name
        self.min_dam = min_dam
        self.max_dam = max_dam
        self.armor = armor

    def getName(self):
        return self.name

    def getArmor(self):
        return self.armor

    def getDamage(self):
        return random.randint(min_dam, max_dam)

    def examine(self):
        print(self.description)

class HealingItem(Item):
    
    def __init__(self, name, description, health, quantity):
        self.name = name
        self.description = description
        self.health = health
        self.quantity = quantity

    def use(self, playerInstance):
        
        playerInstance.takeDamage(-1*health)

        quantity -= 1

        if quantity == 0:
            del self

    def getQuantity(self):
        return self.quantity
