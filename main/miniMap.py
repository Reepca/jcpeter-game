from room import Room
from util import x, y, WEST, NORTH, EAST, SOUTH

class MiniMap(object):
    
    mapImage = None
    initOffset = [0, 0]
    betweenRooms = 0
    roomSize = 0
    
    def __init__(self, rooms):
        self.rooms = rooms
        
        
    def draw(self, drawCoord=(300, 200), dimensions=(300, 200)):
        centerPos = [drawCoord[x] + dimensions[x]/2, drawCoord[y] + dimensions[y]/2]
        rectMode(CENTER)
        for room in self.rooms:
            if room.discovered:
                fill(0, 255, 0)
            if room.visited:
                fill(0, 0, 255)
            if Room.currentRoom == room:
                fill(255, 255, 0)
            xPos = centerPos[x] + room.gridCoord[x] * (MiniMap.roomSize + MiniMap.betweenRooms)
            yPos = centerPos[y] + room.gridCoord[y] * (MiniMap.roomSize + MiniMap.betweenRooms)
            if room.discovered:
                rect(xPos, yPos, MiniMap.roomSize, MiniMap.roomSize)
        fill(0)
        rectMode(CORNER)
        
        
def updateMiniMap():
        for direction in range(WEST, SOUTH+1):
            if Room.currentRoom.adjRooms[direction] != None and Room.currentRoom.doors[direction] != None:
                Room.currentRoom.adjRooms[direction].discovered = True
                
        
def initMiniMap():
    #MiniMap.mapImage = loadImage("miniMap.png")
    MiniMap.initOffset = [0, 0]
    MiniMap.betweenRooms = 5
    MiniMap.roomSize = 40