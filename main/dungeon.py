from util import NO_DIR, WEST, EAST, SOUTH, NORTH, x, y, AJAR, CLOSED, opposite
from room import Door
from room import Room


class Dungeon(object):
    
    def __init__(self, roomCount):
        self.roomCount = roomCount

        # list of all rooms in dungeon.. maybe restructure this later
        self.rooms = []
        
        # initial start room creation
        self.rooms.append(Room(gridCoord=[0, 0], currentRoom=True))
        
        # this enter is actually not needed, but i'm going to keep it around just in case
        #self.rooms[0].enter(NO_DIR)
        
        # add two rooms
        self.addRoom(Room.currentRoom, Room.PUZZLE, EAST)
        self.addRoom(self.rooms[1],Room.END, SOUTH, [True, True, True, False])
        self.addRoom(self.rooms[0], Room.PUZZLE, SOUTH)
        
        # notice that rooms[2] and rooms[3] should connect, this is what linkRooms and 
        # the gridCoords are for.
            
    def addRoom(self, adjRoom, type, direction=NO_DIR, doors=[True, True, True, True]):
        print "Add Room Called"
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
        
        
        newDoors = []
        if not alreadyExists:
            # make the doors
            for i in range(len(doors)):
                if doors[i]:
                    newDoors.append(Door(i))
                else:
                    newDoors.append(None)
            
            # make the room
            newRoom = Room(direction, type, None, gridCoord, doors=newDoors)
        
            # update pointers
            if direction != NO_DIR:
                adjRoom.adjRooms[direction] = newRoom
                newRoom.adjRooms[opposite(direction)] = adjRoom
            
            self.rooms.append(newRoom)
            self.linkRooms(newRoom)

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
                    
    print "finished dungeon"