from util import NO_DIR, WEST, EAST, SOUTH, NORTH, x, y, AJAR, CLOSED
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
        if self.direction == NORTH:
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
        elif self.direction == WEST:
            if self.state == AJAR:
                image(Door.westDoorOpen, 0,
                      height/2 - Door.westDoorOpen.height/2)
            else:
                image(Door.westDoorClosed, 0,
                  height/2 - Door.westDoorClosed.height/2)

    def toggleOpen(self):
        self.state = not self.state


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

    def __init__(self, enterDirection=NO_DIR, type=START, doors=None):
        """ """
        if doors:
            self.doors = doors
        else:
            self.doors = [Door(WEST), Door(EAST), Door(SOUTH), Door(NORTH)]
        super(Room, self).__init__((Room.wallDepth,
                                    Room.wallDepth, width - Room.wallDepth,
                                    height - Room.wallDepth),
                                   self,
                                   location=(width/2,
                                             height/2)) 
        self.type = type
        self.enterDirection = enterDirection
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

        for door in self.doors:
            door.drawSprite()

    def updateDoor(self, direction, state):
        """ """
        self.doors[direction].state = state

    def toggleDoor(self, direction):
        self.doors[direction].state = not self.doors[direction].state




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
                           height/2 - Door.eastDoorOpen.height/2,
                           Room.wallDepth,
                           height/2 + Door.eastDoorOpen.height/2))
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
    # North
    Door.doorZones.append((width/2 - Door.northDoorOpen.width/2,
                           0,
                           width/2 + Door.northDoorOpen.width/2,
                           Room.wallDepth))


def initRoom():
        """Annoyingly enough, we can't use loadImage() until at least setup()
        time."""
        Room.startRoom = loadImage("startRoom.png")
        initDoor()
