from util import NO_DIR, WEST, EAST, SOUTH, NORTH, x, y, AJAR, CLOSED
from sprite import Sprite

class Room(Sprite):
    
    # Wall depth in pixels
    wallDepth = 75
    
    currentRoom = None
    
    # All rooms
    allRooms = []
    
    # Some enums for the types of rooms
    START = 0
    PUZZLE = 1
    BATTLE = 2
    EMPTY = 3
    END = 4
    
    # Room images
    startRoom = None
    puzzleRoom = None
    endRoom = None
    
    # Door images
    # Loading only works as early as setup(), unfortunately, so this has to
    # be put off until then... see initRoom() at bottom of file.
    # https://github.com/processing/processing/issues/4501
    northDoorOpen = None
    northDoorClosed = None
    eastDoorOpen = None
    eastDoorClosed = None
    southDoorOpen = None
    southDoorClosed = None
    westDoorOpen = None
    westDoorClosed = None
    
    # Door zones 
    northDoorZone = None
    eastDoorZone = None
    southDoorZone = None
    westDoorZone = None
    
    def __init__(self, enterDirection=NO_DIR, type=START, doorStates=[False, False, False, False]):
        """ """
        super(Room, self).__init__((Room.wallDepth, Room.wallDepth, width - Room.wallDepth, height - Room.wallDepth), self, location=(width/2, height/2))
        self.type = type
        self.enterDirection = enterDirection
        self.doorStates = doorStates
        Room.allRooms.append(self)
        
        
    def enter(self, enterDirection):
        self.enterDirection = enterDirection
        Room.currentRoom = self
        self.updateDoor(enterDirection, AJAR)

    def draw(self, arg1, arg2):
        # draw the background image based on room type
        drawImg = Room.startRoom
        if type == Room.START:
            pass
        elif type == Room.PUZZLE:
            pass
        elif type == Room.END:
            pass
        image(drawImg, 0, 0)
            
        # draw the doors in their state
        if self.doorStates[NORTH]:
            image(Room.northDoorOpen, width/2 - Room.northDoorOpen.width/2, 0)
        else:
            image(Room.northDoorClosed, width/2 - Room.northDoorClosed.width/2, 0)
        if self.doorStates[EAST]:
            image(Room.eastDoorOpen, width - Room.eastDoorOpen.width, height/2 - Room.eastDoorOpen.height/2)
        else:
            image(Room.eastDoorClosed,width - Room.eastDoorClosed.width, height/2 - Room.eastDoorClosed.height/2)
        if self.doorStates[SOUTH]:
            image(Room.southDoorOpen, width/2 - Room.southDoorOpen.width/2, height - Room.southDoorOpen.height)
        else:
            image(Room.southDoorClosed, width/2 - Room.southDoorClosed.width/2, height - Room.southDoorClosed.height)
        if self.doorStates[WEST]:
            image(Room.westDoorOpen, 0, height/2 - Room.westDoorOpen.height/2)
        else:
            image(Room.westDoorClosed, 0, height/2 - Room.westDoorClosed.height/2)
            
            
    def updateDoor(self, direction, state):
        """ """
        self.doorStates[direction] = state
        
        
    def toggleDoor(self, direction):
        self.doorStates[direction] = not self.doorStates[direction]
        
        
def initRoom():
        """Annoyingly enough, we can't use loadImage() until at least setup() time."""
        Room.startRoom = loadImage("startRoom.png")
        Room.northDoorOpen = loadImage("northDoorOpen.png")
        Room.northDoorClosed = loadImage("northDoorClosed.png")
        Room.eastDoorOpen = loadImage("eastDoorOpen.png")
        Room.eastDoorClosed = loadImage("eastDoorClosed.png")
        Room.southDoorOpen = loadImage("southDoorOpen.png")
        Room.southDoorClosed = loadImage("southDoorClosed.png")
        Room.westDoorOpen = loadImage("westDoorOpen.png")
        Room.westDoorClosed = loadImage("westDoorClosed.png")
        
        Room.northDoorZone = (width/2 - Room.northDoorOpen.width/2, 0, width/2 + Room.northDoorOpen.width/2, Room.wallDepth)
        Room.eastDoorZone = (width - Room.eastDoorOpen.width, height/2 - Room.eastDoorOpen.height/2, width, height/2 + Room.eastDoorOpen.height/2)
        Room.southDoorZone = (width/2 - Room.southDoorOpen.width/2, height - Room.southDoorOpen.height, width/2 + Room.southDoorOpen.width/2, height)
        Room.westDoorZone = (0, height/2 - Room.eastDoorOpen.height/2, Room.wallDepth, height/2 + Room.eastDoorOpen.height/2)