# File: main.py
'''Description: This program is going to be the main source file for our game.
The only built in functions will be in here (like draw, setup, keyPressed, etc).
'''


# Imports
import sprite
import character
import room
from util import NORTH, WEST, EAST, SOUTH, CLOSED, AJAR

# Ugly globals
key_states = dict()
timeOfLastUpdate = millis()
player = None
firstRoom = None
test = 0
enterDoor = False

def setup():
    size(800, 800)
    # When we try doing this outside of setup(), for some reason we end up with
    # 2 invocations of Character()... and for some reason dict() doesn't work
    # either.
    # Ugly hack
    room.initRoom()
    global player, firstRoom
    firstRoom = room.Room()
    firstRoom.enter(WEST)
    player = character.Character()


def draw():
    global timeOfLastUpdate, test, player, enterDoor
    background(30, 50, 130)
    update(millis() - timeOfLastUpdate)
    timeOfLastUpdate = millis()
    sprite.drawAllSprites()


def keyPressed():
    global key_states
    # Adjust player velocity based on arrow key states
    # (UP, DOWN, LEFT, RIGHT)
    if key == 'q' or key == 'Q':
        player.triggerDoorToggle()

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

    else:
        key_states[key] = True


def keyReleased():
    global key_states
    if key == CODED:
        key_states[keyCode] = False
        if not (key_states.get(UP) or key_states.get(DOWN)):
            player.setWalkY(None)
        if not (key_states.get(LEFT) or key_states.get(RIGHT)):
            player.setWalkX(None)
    else:
        key_states[key] = False    


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