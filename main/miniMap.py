from room import Room
from util import x, y, WEST, NORTH, EAST, SOUTH, median

class MiniMap(object):
    
    mapImage = None
    mapBorder = [0, 0]
    spaceRatio = 8
    
    def __init__(self, rooms):
        self.rooms = rooms
        self.mapSize = (MiniMap.mapImage.width - 2 * MiniMap.mapBorder[x], MiniMap.mapImage.height - 2 * MiniMap.mapBorder[y])
        
        self.xGridCoords = []
        self.yGridCoords = []        
        for room in self.rooms:
            if self.xGridCoords.count(room.gridCoord[x]) == 0:
                self.xGridCoords.append(room.gridCoord[x])
            if self.yGridCoords.count(room.gridCoord[y]) == 0:
                self.yGridCoords.append(room.gridCoord[y])
        self.xGridCoords.sort()
        self.yGridCoords.sort()
        
        self.minimums = [min(self.xGridCoords), min(self.yGridCoords)]
        self.maximums = [max(self.xGridCoords), max(self.yGridCoords)]
        
        self.roomCount = (abs(self.maximums[x]) + abs(self.minimums[x]) + 1,
                          abs(self.maximums[y]) + abs(self.minimums[y]) + 1)
        
        self.roomSize = min(MiniMap.spaceRatio * self.mapSize[x] / ((MiniMap.spaceRatio + 1) * self.roomCount[x] - 1),
                         MiniMap.spaceRatio * self.mapSize[y] / ((MiniMap.spaceRatio + 1) * self.roomCount[y] - 1))
        
        self.spaceSize = min(self.roomSize / MiniMap.spaceRatio,
                             self.roomSize / MiniMap.spaceRatio)
        
        self.shift = [median(self.xGridCoords) * (self.roomSize + self.spaceSize), 
                 median(self.yGridCoords) * (self.roomSize + self.spaceSize)]
        print(median(self.xGridCoords), median(self.yGridCoords))
        
        
    def draw(self, drawCoord=(125, 125)):
        image(MiniMap.mapImage, drawCoord[x], drawCoord[y])
        
        centerPos = [drawCoord[x] + MiniMap.mapImage.width/2 - self.shift[x],
                     drawCoord[y] + MiniMap.mapImage.height/2 - self.shift[y]]
        rectMode(CENTER)
        textAlign(CENTER)
        for room in self.rooms:
            rectColor = color(0)
            fontColor = color(0)
            if room.discovered:
                rectColor = color(0, 255, 0)
                fontColor = color(0)
            if room.visited:
                rectColor = color(0, 0, 255)
                fontColor = color(255)
            if Room.currentRoom == room:
                rectColor = color(255, 255, 0)
                fontColor = color(0)
            xPos = centerPos[x] + room.gridCoord[x] * (self.roomSize + self.spaceSize)
            yPos = centerPos[y] + room.gridCoord[y] * (self.roomSize + self.spaceSize)
            if room.discovered:
                fill(rectColor)
                rect(xPos, yPos, self.roomSize, self.roomSize)
                fill(fontColor)
                text(str(room.roomId), xPos,yPos)
            fill(50)
            rectMode(CORNER)
            if room.visited:
                for direction in range(WEST, SOUTH+1):
                    if room.doors[direction] != None:
                        if direction == WEST:
                            rect(xPos - self.roomSize/2 - self.spaceSize,
                                yPos - self.spaceSize,
                                self.spaceSize,
                                self.spaceSize)
                        elif direction == NORTH:
                            rect(xPos - self.spaceSize,
                                yPos - self.roomSize/2 - self.spaceSize,
                                self.spaceSize,
                                self.spaceSize)
                        elif direction == EAST:
                            rect(xPos + self.roomSize/2,
                                yPos - self.spaceSize,
                                self.spaceSize,
                                self.spaceSize)
                        elif direction == SOUTH:
                            rect(xPos - self.spaceSize,
                                yPos + self.roomSize/2,
                                self.spaceSize,
                                self.spaceSize)
            rectMode(CENTER)
                    
        fill(0)
        
        
        
def updateMiniMap():
        for direction in range(WEST, SOUTH+1):
            if Room.currentRoom.adjRooms[direction] != None and Room.currentRoom.doors[direction] != None:
                Room.currentRoom.adjRooms[direction].discovered = True
                
        
def initMiniMap():
    MiniMap.mapImage = loadImage("miniMap.png")
    MiniMap.mapBorder = [30, 30]
    