# File: main.py
''' Description: This program is going to be the main source file for our game.
The only built in functions will be in here (like draw, setup, keyPressed, etc).
'''

#Imports
import character
import sprite

# Ugly globals
key_states = dict()
player = character.character()
hit = False


def setup():
    size(800, 800)


def draw():
    background(30, 50, 130)
    ellipse(player.x, player.y, 30, 30)
    
    # Adjust player position based on arrow key states
    # (UP, DOWN, LEFT, RIGHT)
    if key_states.get(UP):
        player.y -= player.speed
    elif key_states.get(DOWN):
        player.y += player.speed
    if key_states.get(LEFT):
        player.x -= player.speed
    elif key_states.get(RIGHT):
        player.x += player.speed
        
    # Sword attack (SPACE)
    if hit == True:
        rect(10, 10, 10, 10)


def keyPressed():
    global hit
    key_states[keyCode] = True
    if(key == ' '):
        print(hit)
        hit = True

            
def keyReleased():
    global hit
    key_states[keyCode] = False
    hit = False


def main():
    pass



# The main() call of destiny
main()