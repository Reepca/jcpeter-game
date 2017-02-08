# File: main.py
''' Description: This program is going to be the main source file for our game.
The only built in functions will be in here (like draw, setup, keyPressed, etc).
'''

#Imports
import character
from sprite import Sprite
from util import x, y, NORTH, WEST, EAST, SOUTH

# Ugly globals
key_states = dict()
player = character.Character()
timeOfLastUpdate = millis()



def setup():
    size(800, 800)


def draw():
    background(30, 50, 130)
    update(millis() - timeOfLastUpdate)
    timeOfLastUpdate = millis()
    Sprite.drawAllSprites()


def keyPressed():
    # Adjust player velocity based on arrow key states
    # (UP, DOWN, LEFT, RIGHT)
    if key == CODED:
        key_states[keyCode] = True
        if keyCode == UP:
            player.setWalkY(NORTH)
        elif keyCode == DOWN:
            player.setWalkY(SOUTH)
        if keyCode == LEFT:
            player.setWalkX(WEST)
        elif keyCode == RIGHT:
            player.setWalkX(EAST)

def keyReleased():
    if key == CODED:
        key_states[keyCode] = False
        if not (key_states[UP] or key_states[DOWN]):
            player.setWalkY(None)
        if not (key_states[LEFT] or key_states[RIGHT]):
            player.setWalkY(None)
    
def update(timePassed):
    """timePassed is the amount of time passed since last update (in
    milliseconds)"""
    character.updatePositions(timePassed)

    
def main():
    # The actual entry point to the program isn't really clear, so here we'll
    # just describe what order we expect Processing to automagically call stuff
    # in.

    # 1. setup()
    # 2. draw(), check for events like keyPressed, call the associated event
    # handlers (keyPressed(), keyReleased(), mousePressed(), mouseReleased(),
    # mouseClicked(), etc)
    # 3. Repeat 2 until the window is closed or escape is pressed or some other
    # thing that would indicate it should stop.
    pass



# The main() call of destiny (doesn't do anything)
main()
