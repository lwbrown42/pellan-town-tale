import character

class Area:

    dirs = ['north', 'south', 'east', 'west', 'up', 'down']
    movepath = {}

    enemyList = []
    npcList = []
    

    def __init__(self):
        self._load_zone("area1/area1.txt")
       
    def _load_zone(self, zonepath):
        self.npcList = []
        self.enemyList = []

        areaFile = open(zonepath, 'r')

        for line in areaFile:
            lineparse = line.split(":")
        
            line0 = lineparse[0]
            line1 = lineparse[1][1:-1]

            if line0 == 'name':
                self.name = line1
            elif line0 == 'description':
                self.description = line1
            elif line0 == 'npc':
                if line1 != 'none':
                    newNPC = character.NPC(line1.strip())
                    self.npcList.append(newNPC)
                else:
                    self.npcList.append('none')
            elif line0 == 'enemy':
                if line1 != 'none':
                    enemyNPC = character.Enemy(line1.strip())
                    self.enemyList.append(enemyNPC)
                else:
                    self.enemyList.append('none')
            elif line0 in self.dirs:
                self.movepath[line0] = line1

    def getPrevious(self):
        return self.previous

    def getEnemies(self):
        return self.enemyList
        
    def getNPC(self):
        return self.npcList
        
    def examine(self):
        print("------ " + self.name + " -------")
        print("")
        print(self.description)
        if self.npcList[0] != 'none':
            print("")
            print("There is a " + self.npcList[0].getName() + " in this area.")

    def move(self, direction):
        if self.movepath[direction] != 'none':
            self._load_zone(self.movepath[direction])
            if direction == 'north':
                self.previous = 'south'
            elif direction == 'south':
                self.previous = 'north'
            elif direction == 'east':
                self.previous = 'west'
            else:
                self.previous = 'east'
        else:
            print("You cannot go in that direction.")

        self.examine()

    def killEnemies(self):
        self.enemyList[0] = 'none'
