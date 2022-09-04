import random
import time

def showIntro():
    print('''You are in the land of Dragon. In front of you will see two caves. In one of them, you will find a friendly dragon and it will share treasures with you. At another one you will find an angry and hungry dragon and you will be eaten by it. You have to choose which cave you are heading to. Good luck!''')
    print()

def chooseCave():
    cave = ''
    while cave != 1 and cave != 2:
        print('Which cave you will enter into? (1 or 2?)')
        cave = input ()
        return cave
    
def checkCave(chosenCave):
    print('You approach to the cave...')
    time.sleep(2)
    print ('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps on you. He opens his jaws and ...')
    print()
    time.sleep(2)
    
    friendlyCave = random.randint(1, 2)
    
    if chosenCave == str (friendlyCave):
        print ('Gives his treasures!')
    else:
        print ('Gobbles you down in one bite')
        
playAgain = 'yes'
while playAgain =='yes'  or playAgain == 'y':
    showIntro()
    caveNumber = chooseCave()
    checkCave (caveNumber)
    
    print('Do you want to play again? (yes or no?)')
    playAgain = input()
    