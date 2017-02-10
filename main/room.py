from util import NO_DIR, WEST, EAST, SOUTH, NORTH, x, y
from sprite import Sprite

class Room(Sprite):
    
    
    # All rooms
    allRooms = []
    
    # Some enums for the types of rooms
    START = 0
    PUZZLE = 1
    BATTLE = 2
    EMPTY = 3
    END = 4
    
    # Room images
    startRoom = loadImage("startRoom.png")
    puzzleRoom = None
    endRoom = None
    
    # Door images
    northDoorOpen = loadImage("northDoorOpen.png")
    northDoorClosed = loadImage("northDoorClosed.png")
    eastDoorOpen = loadImage("eastDoorOpen.png")
    eastDoorClosed = loadImage("eastDoorClosed.png")
    southDoorOpen = loadImage("southDoorOpen.png")
    southDoorClosed = loadImage("southDoorClosed.png")
    westDoorOpen = loadImage("westDoorOpen.png")
    westDoorClosed = loadImage("westDoorClosed.png")
    
    def __init__(self, enterDirection, type=START, doorStates=[False, False, False, False]):
        """ """
        self.type = type
        self.enterDirection = enterDirection
        self.doorStates = doorStates
        
    def load(self):
        """ """
        
    def draw():
        
        # draw the background image based on room type
        drawImg = startRoom
        if type == START:
            pass
        elif type == PUZZLE:
            pass
        elif type == END:
            pass
        image(drawImg, 0, 0)
            
        # draw the doors in their state
        if doorStates[NORTH]:
            image(northDoorOpen,0,0)
        else:
            image(northDoorClosed,0,0)
        if doorStates[EAST]:
            image(eastDoorOpen,0,0)
        else:
            image(eastDoorClosed,0,0)
        if doorStates[SOUTH]:
            image(southDoorOpen,0,0)
        else:
            image(southDoorClosed,0,0)
        if doorStates[WEST]:
            image(westDoorOpen,0,0)
        else:
            image(westDoorClosed,0,0)
            
            
    def updateDoor(self, direction, state):
        """ """
        self.doorStates[direction] = state