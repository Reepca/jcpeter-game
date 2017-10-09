from util import NO_DIR, WEST, EAST, SOUTH, NORTH, x, y, AJAR, CLOSED, opposite
from room import Door
from room import Room
from jkey import Key
import random as r

class Dungeon(object):
    def __init__(self, roomCount):
        self.roomCount = roomCount

        # list of all rooms in dungeon.. maybe restructure this later
        self.rooms = []
        self.roomKeys = []
        
        self.generateDungeon(roomCount)
        
        # notice that rooms[2] and rooms[3] should connect, this is what linkRooms and 
        # the gridCoords are for.
        
            
    def generateDungeon(self, roomCount):
        """ """
        print "Generating Dungeon"
        # initial start room creation
        self.rooms.append(Room(gridCoord=[0, 0], currentRoom=True))
        
        # populate rooms list
        while len(self.rooms) != roomCount:
            # random existing room to add on to (0-len(rooms[]-1))
            chosenRoom = r.randint(0, len(self.rooms) - 1)
            # random room type (0-4)
            roomType = r.randint(Room.START, Room.END)
            # random direction (0-3)
            roomDir = r.randint(WEST, SOUTH)
            if(self.addRoom(self.rooms[chosenRoom], roomType, roomDir)):
                room = r.randint(0, len(self.rooms) - 2)
                xPos = r.randint(Room.currentRoom.boundingBox[0] + Key.keyImg.width/2,
                                 Room.currentRoom.boundingBox[2] - Key.keyImg.width/2)
                yPos = r.randint(Room.currentRoom.boundingBox[1] + Key.keyImg.width/2,
                                 Room.currentRoom.boundingBox[3] - Key.keyImg.width/2)
                self.roomKeys.append(Key(xPos, yPos, self.rooms[room]))
                
    
            
    def addRoom(self, adjRoom, type, direction=NO_DIR):
        # print "Add Room Called"
        # assign the room new coords relative to the adjacent room 
        gridCoord = [0, 0]
        # if the new room is to the west of adjRoom
        if direction == WEST:
            gridCoord[x] = adjRoom.gridCoord[x] - 1
            gridCoord[y] = adjRoom.gridCoord[y]
        # if the new room is to the north of adjRoom
        elif direction == NORTH:
            gridCoord[x] = adjRoom.gridCoord[x]
            gridCoord[y] = adjRoom.gridCoord[y] - 1
        # if the new room is to the east of adjRoom
        elif direction == EAST:
            gridCoord[x] = adjRoom.gridCoord[x] + 1
            gridCoord[y] = adjRoom.gridCoord[y]
        # if the new room is to the south of adjRoom
        elif direction == SOUTH:
            gridCoord[x] = adjRoom.gridCoord[x]
            gridCoord[y] = adjRoom.gridCoord[y] + 1
        
        alreadyExists = False
        for room in self.rooms:
            if room.gridCoord == gridCoord:
                alreadyExists = True
        
        if not alreadyExists:
            # make the room
            newRoom = Room(direction, type, None, gridCoord)
        
            # update pointers
            if direction != NO_DIR:
                adjRoom.adjRooms[direction] = newRoom
                newRoom.adjRooms[opposite(direction)] = adjRoom
            
            self.rooms.append(newRoom)
            self.linkRooms(newRoom)
        
        return True if not alreadyExists else False
        
    def linkRooms(self, linkRoom):
        """ """
        for room in self.rooms:
            
            if room.gridCoord[x] == linkRoom.gridCoord[x]:
                # there is a room north of link room
                if room.gridCoord[y] == linkRoom.gridCoord[y] - 1:
                    room.adjRooms[SOUTH] = linkRoom
                    linkRoom.adjRooms[NORTH] = room
                # there is a room south of linkRoom
                elif room.gridCoord[y] == linkRoom.gridCoord[y] + 1:
                    room.adjRooms[NORTH] = linkRoom
                    linkRoom.adjRooms[SOUTH] = room
            if room.gridCoord[y] == linkRoom.gridCoord[y]:
                # there is a room west of link room
                if room.gridCoord[x] == linkRoom.gridCoord[x] - 1:
                    room.adjRooms[EAST] = linkRoom
                    linkRoom.adjRooms[WEST] = room
                # there is a room east of linkRoom
                elif room.gridCoord[x] == linkRoom.gridCoord[x] + 1:
                    room.adjRooms[WEST] = linkRoom
                    linkRoom.adjRooms[EAST] = room
                    