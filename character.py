import item

class Character:

    def __init__(self):

        self.health = 0
        self.max_health = 10
        self.name = ""
        self.state = "Healthy"
        self.armor = 15
    
    def takeDamage(self, damage):
        self.health -= damage
        
    def _updateState(self):
        if self.health <= self.max_health and self.health >= (self.max_health*.75):
            self.state = "Healthy"
        elif self.health >= (self.max_health*.5):
            self.state = "Wounded"
        elif self.health >= (self.max_health*.25):
            self.state = "Ragged"
        elif self.health > 0:
            self.state = "Severe"
        else:
            self.state = "Dead"

    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def getArmor(self):
        return self.armor

class Player(Character):
    
    def __init__(self):

        self.health = 10
        self._createCharacter()
        self.max_health = 10
        self._updateState()
        self.armor = 10
        self.level = 1
        self.experience = 0
        self.nextlevel = 100

        longsword = item.Item('longsword', 'Your trusty sword.', 4, 11, 0)
        shield = item.Item('kite shield', 'Your trusty shield.', 0, 0, 10)
        potions = item.HealingItem('potion', 'A red liquid in a bottle. Tastes a little spicy.', 10, 20)

        self.inventory = [longsword, shield, potions]

    def giveXP(self, xp):
        self.experience += xp
    
        if self.experience >= self.nextlevel:
            self.level += 1
            self.nextlevel = level * 100
            self.max_health += 5
            self.health = self.max_health
            print("Congratulations! You've reached level " + str(self.level))

    def status(self):
        print ("Status:" + self.state)
        
    def _createCharacter(self):
        self.name = input("What is your name?\n")
        self.age = input("What is your age?\n")
        ready = input("Are you prepared for your quest? (y/n)\n")

        if ready == 'y':
            print("Let us begin!")
        elif ready == 'n':
            print("Oh well!")
        else:
            print("I don't understand.")

    def displayInventory(self):
        print("Your inventory:")
        for i in self.inventory:
            if type(i) == item.HealingItem:
                print("- " + i.getName() + " x" + str(i.getQuantity()))
            else:
                print("- " + i.getName())
            

    
class Enemy(Character):    

    def __init__(self, enemyType):
        self._loadEnemy(enemyType)
        self.state = self._updateState()

    def _loadEnemy(self, enemyType):
        enemyPath = "enemies/" + enemyType + ".txt"
        

        infile = open(enemyPath, 'r')
        for line in infile:
            line0, line1 = line.split(':')
            line1 = line1[1:-1]

            if line0 == 'name':
                self.name = line1
            elif line0 == 'max_health':
                self.max_health = int(line1)
                self.health = int(line1)
            elif line0 == 'evasion':
                self.evasion = int(line1)
            elif line0 == 'armor':
                self.armor = int(line1)
            elif line0 == 'description':
                self.description = line1

    def getEvasion(self):
        return self.evasion

class NPC(Character):

    eatStr = "none"
    smellStr = "none"
    talkStr = "none"
    description = "none"

    def __init__(self, npcType):
        self._loadNPC(npcType)
        

    def _loadNPC(self, npcType):
        npcPath = "npcs/" + npcType + ".txt"
    
        infile = open(npcPath, 'r')
        for line in infile:
            line0, line1 = line.split(':')
            line1 = line1[1:-1]

            if line0 == 'name':
                self.name = line1
            elif line0 == 'description':
                self.description = line1
            elif line0 == 'eat':
                self.eatStr = line1
            elif line0 == 'smell':
                self.smellStr = line1
            elif line0 == 'talk':
                self.talkStr = line1

    def getActionDict(self):
        return self.actionDict

    def examine(self):
        print(self.description)
        print("")

    def eat(self):
        if self.eatStr != "none":
            print(self.eatStr)
        else:
            print("You can't eat them.")
        
        print("")

    def smell(self):
        if self.smellStr != "none":
            print(self.smellStr)
        else:
            print("You can't smell the " + self.name)
        
        print("")

    def talk(self):
        if self.talk != "none":
            print(self.talkStr)
        else:
            print("The " + self.name + " ignores you.")
        
        print("")

    actionDict = {'examine': examine, 'eat': eat, 'smell': smell, 'talk': talk}
