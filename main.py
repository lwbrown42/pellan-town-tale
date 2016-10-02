#!/usr/bin/env python3

import area
import character
import random

currentArea = area.Area()
player = character.Player()

def playerTurn():
    command = input("What would you like to do:\n").lower()

    commandUnderstood = True

    if len(command.split()) == 1:
        if command in ['north', 'n']:
            currentArea.move('north')
        elif command in ['south', 's']:
            currentArea.move('south')
        elif command in ['east', 'e']:
            currentArea.move('east')
        elif command in ['west', 'w']:
            currentArea.move('west')
        elif command == 'examine':
            currentArea.examine()
        elif command == "status":
            player.status()
        elif command == 'inventory':
            inventory()
        elif command == "quit":
            exit()
        else:
            commandUnderstood = False

    elif len(command.split()) > 0:
        
        #need to determine what the noun was
        
        commandList = command.split()

        for item in currentArea.getNPC():
            if item != 'none' and item.getName() == commandList[1]:
                commandHelper(item, commandList[0])
                return
    else:
        commandUnderstood = False

    if not commandUnderstood:
        print("Unknown command.")

def commandHelper(noun, verb):

    actionDict = noun.getActionDict()
    if verb in actionDict.keys():
        foundAction = actionDict[verb]
        foundAction(noun)

def combat():

    inCombat = True

    print("\n------ Combat Started -------\n\n")

    enemyNPC = currentArea.getEnemies()[0]

    npcName = enemyNPC.getName()
    npcArmor = enemyNPC.getArmor()
    npcEvasion = enemyNPC.getEvasion()

    playerArmor = player.getArmor()

    print("An enemy approaches! A " + npcName + " confronts you!.")
    print("")

    while enemyNPC.getHealth() > 0 and inCombat == True:
        invalidInput = True

        while invalidInput:
            command = input("Attack or run?\n").lower()
            print("")
            if command == "attack":
                invalidInput = False
                print("You swing your sword!")
                
                damageRoll = random.randint(0,20)
                if damageRoll > npcArmor:
                    damage = random.randint(2,6)
                    print("You do " + str(damage) + " damage to the " + npcName + "!\n")
                    enemyNPC.takeDamage(damage)

                    if enemyNPC.getHealth() <= 0:
                        break
                else:
                    print("The " + npcName + " blocked your attack!\n")
            elif command == "run":
                invalidInput = False
                print("You attempt to run away!")
                runattempt = random.randint(0,20)
                if runattempt > npcEvasion:
                    print("You manage to escape!")
                    print("\n------ Combat Ended ------\n\n") 
                    currentArea.move(currentArea.getPrevious())
                    return
                else:
                    print("Failed to escape!\n")
            else:
                print("Invalid command.")
            

        if enemyNPC.getHealth() > 0:
            print("The " + npcName + " swings at you!")
            damageRoll = random.randint(0,20)
            if damageRoll > playerArmor:
                damage = random.randint(1, 4)
                print("The " + npcName + " hits and does " + str(damage) + " damage to you!\n")
                player.takeDamage(damage)
            else:
                print("You block the attack!\n")
    
    print("You have defeated the " + npcName + "!\n")
    
    currentArea.killEnemies()

    print("\n------ Combat Ended ------\n\n")

    del enemyNPC

def gamestart():
    
    currentArea.examine()

    while True:
        if currentArea.getEnemies()[0] == 'none':
            playerTurn()
        else:
            combat()
            


def main():

    gamestart()

main()
