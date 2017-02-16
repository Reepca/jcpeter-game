from util import NO_DIR, WEST, EAST, SOUTH, NORTH, x, y, AJAR, CLOSED
from room import Door
from room import Room

class Dungeon(object):
    def __init__(self, roomCount):
        self.roomCount = roomCount
        
        roomType = Room.START
        # Populate this dungeon's list of rooms
        self.rooms = []
        self.addRoom(Room.currentRoom, Room.PUZZLE, EAST)
        
            
    def addRoom(self, adjRoom, type, direction=NO_DIR):
        
        # assign the room new coords relative to the adjacent room 
        gridCoord = [0, 0]
        # if the new room is to the west of adjRoom
        if direction == WEST:
            gridCoord[x] = adjRoom.gridCoord[x] - 1
            gridCoord[y] = adjRoom.gridCoord[y]
        # if the new room is to the east of adjRoom
        elif direction == EAST:
            gridCoord[x] = adjRoom.gridCoord[x] + 1
            gridCoord[y] = adjRoom.gridCoord[y]
        # if the new room is to the south of adjRoom
        elif direction == SOUTH:
            gridCoord[x] = adjRoom.gridCoord[x]
            gridCoord[y] = adjRoom.gridCoord[y] + 1
        # if the new room is to the north of adjRoom
        elif direction == NORTH:
            gridCoord[x] = adjRoom.gridCoord[x]
            gridCoord[y] = adjRoom.gridCoord[y] - 1
            
        # make the room
        newRoom = Room(direction, type, None, gridCoord)
        
        # update pointers
        if direction != NO_DIR:
            adjRoom.adjRooms[direction] = newRoom
            oppositeDir = NO_DIR
            oppositeDir = EAST if direction == WEST else oppositeDir
            oppositeDir = NORTH if direction == SOUTH else oppositeDir
            oppositeDir = SOUTH if direction == NORTH else oppositeDir
            oppositeDir = WEST if direction == EAST else oppositeDir
            newRoom.adjRooms[oppositeDir] = adjRoom
        
        self.rooms.append(newRoom)
        
    def relinkRooms(self):
        """ """