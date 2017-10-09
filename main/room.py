from util import NO_DIR, WEST, EAST, SOUTH, NORTH, x, y, AJAR, CLOSED, opposite
from sprite import Sprite

class Door(Sprite):
    # Door images
    # Loading only works as early as setup(), unfortunately, so this has to
    # be put off until then... see initRoom() at bottom of file.
    # https://github.com/processing/processing/issues/4501
    northDoorOpen = None
    northDoorClosed = None
    eastDoorOpen = None
    eastDoorClosed = None
    westDoorOpen = None
    westDoorClosed = None
    southDoorOpen = None
    southDoorClosed = None
    doorZones = []

    def __init__(self, direction, initState=CLOSED):
        super(Door, self).__init__(Door.doorZones[direction], self,
                                   manageInSprite=False)
        self.state = initState
        self.direction = direction

    def draw(self, x, y):
        if self.direction == WEST:
            if self.state == AJAR:
                image(Door.westDoorOpen, 0,
                      height/2 - Door.westDoorOpen.height/2)
            else:
                image(Door.westDoorClosed, 0,
                  height/2 - Door.westDoorClosed.height/2)
        elif self.direction == NORTH:
            if self.state == AJAR:
                image(Door.northDoorOpen, width/2 - Door.northDoorOpen.width/2,
                      0)
            else:
                image(Door.northDoorClosed, width/2 -
                      Door.northDoorClosed.width/2, 0)
        elif self.direction == EAST:
            if self.state == AJAR:
                image(Door.eastDoorOpen, width - Door.eastDoorOpen.width,
                      height/2 - Door.eastDoorOpen.height/2)
            else:
                image(Door.eastDoorClosed, width - Door.eastDoorClosed.width,
                      height/2 - Door.eastDoorClosed.height/2)
        elif self.direction == SOUTH:
            if self.state == AJAR:
                image(Door.southDoorOpen, width/2 - Door.southDoorOpen.width/2,
                      height - Door.southDoorOpen.height)
            else:
                image(Door.southDoorClosed, width/2 -
                      Door.southDoorClosed.width/2, height -
                      Door.southDoorClosed.height)
       

    def toggleOpen(self):
        #print "Door ", self.direction, "was ", self.state, "now is " not self.state
        self.state = not self.state


class Room(Sprite):

    # Wall depth in pixels
    wallDepth = 75

    currentRoom = None

    # Some enums for the types of rooms
    START = 0
    PUZZLE = 1
    BATTLE = 2
    EMPTY = 3
    END = 4

    # Room images
    startRoom = None
    puzzleRoom = None
    battleRoom = None
    endRoom = None

    def __init__(self, enterDirection=NO_DIR, type=START, doors=None, gridCoord=[None, None], currentRoom=False):
        """ """
        print "Room made"
        if doors:
            self.doors = doors
        else:
            self.doors = [Door(WEST), Door(NORTH), Door(EAST), Door(SOUTH)]
               
        
        super(Room, self).__init__((Room.wallDepth,
                                    Room.wallDepth, width - Room.wallDepth,
                                    height - Room.wallDepth),
                                   self,
                                   location=(width/2,
                                             height/2)) 
        if currentRoom:
            Room.currentRoom = self
        self.wallBounds = [0, 0, 0, 0]
        self.gridCoord = gridCoord
        self.adjRooms = [None, None, None, None]
        self.type = type
        self.enterDirection = enterDirection

    def enter(self, enterDirection):
        # enter a room from a direction 
        self.enterDirection = enterDirection
        Room.currentRoom = self
        print "adjRooms: ", self.adjRooms
        if enterDirection != NO_DIR:
            self.doors[enterDirection].state = AJAR
            if self.adjRooms[enterDirection] != None:
                self.adjRooms[enterDirection].doors[opposite(enterDirection)].state = AJAR
        print self.gridCoord
        

    def draw(self, arg1, arg2):
        if self == Room.currentRoom:
            # draw the background image based on the type of currentRoom
            drawImg = None
            if Room.currentRoom.type == Room.START:
                drawImg = Room.startRoom
            elif Room.currentRoom.type == Room.PUZZLE:
                drawImg = Room.puzzleRoom
            elif Room.currentRoom.type == Room.BATTLE:
                drawImg = Room.battleRoom
            elif Room.currentRoom.type == Room.EMPTY:
                drawImg = Room.startRoom
            elif Room.currentRoom.type == Room.END:
                drawImg = Room.endRoom
            image(drawImg, 0, 0)
    
            for door in self.doors:
                door.drawSprite()
        
    

    def updateDoor(self, direction, state):
        """ """
        print "Door direction updated:: ", direction
        self.doors[direction].state = state

    def toggleDoor(self, direction):
        print "Door direction toggled:: ", direction
        self.doors[direction].state = not self.doors[direction].state


    def setWallBounds(self):
        self.wallBounds[WEST] = Door.westDoorOpen.width
        self.wallBounds[NORTH] = Door.southDoorOpen.height
        self.wallBounds[EAST] = Door.eastDoorOpen.width
        self.wallBounds[SOUTH] = Door.southDoorOpen.height
        

def initDoor():
    Door.northDoorOpen = loadImage("northDoorOpen.png")
    Door.northDoorClosed = loadImage("northDoorClosed.png")
    Door.eastDoorOpen = loadImage("eastDoorOpen.png")
    Door.eastDoorClosed = loadImage("eastDoorClosed.png")
    Door.southDoorOpen = loadImage("southDoorOpen.png")
    Door.southDoorClosed = loadImage("southDoorClosed.png")
    Door.westDoorOpen = loadImage("westDoorOpen.png")
    Door.westDoorClosed = loadImage("westDoorClosed.png")
    # West
    Door.doorZones.append((0,
                           height/2 - Door.westDoorOpen.height/2,
                           Room.wallDepth,
                           height/2 + Door.westDoorOpen.height/2))
    # North
    Door.doorZones.append((width/2 - Door.northDoorOpen.width/2,
                           0,
                           width/2 + Door.northDoorOpen.width/2,
                           Room.wallDepth))
    # East
    Door.doorZones.append((width - Room.wallDepth,
                           height/2 - Door.eastDoorOpen.height/2,
                           width,
                           height/2 + Door.eastDoorOpen.height/2))
    # South
    Door.doorZones.append((width/2 - Door.southDoorOpen.width/2,
                           height - Room.wallDepth,
                           width/2 + Door.southDoorOpen.width/2,
                           height))


def initRoom():
        """Annoyingly enough, we can't use loadImage() until at least setup()
        time."""
        Room.startRoom = loadImage("startRoom.png")
        Room.puzzleRoom = loadImage("puzzleRoom.png")
        Room.battleRoom = loadImage("battleRoom.png")
        Room.endRoom = loadImage("endRoom.png")
        initDoor()