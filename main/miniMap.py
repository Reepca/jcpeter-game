from room import Room
from util import x, y, WEST, NORTH, EAST, SOUTH, median

class MiniMap(object):
    
    mapImage = None
    discoveredRoom = None
    currentRoomMarker = None
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
        
        
    def draw(self, drawCoord=(125, 125)):
        image(MiniMap.mapImage, drawCoord[x], drawCoord[y])
        
        centerPos = [drawCoord[x] + MiniMap.mapImage.width/2 - self.shift[x],
                     drawCoord[y] + MiniMap.mapImage.height/2 - self.shift[y]]
        textAlign(CENTER)
        imageMode(CENTER)
        for room in self.rooms:

            xPos = centerPos[x] + room.gridCoord[x] * (self.roomSize + self.spaceSize)
            yPos = centerPos[y] + room.gridCoord[y] * (self.roomSize + self.spaceSize)
            if room.discovered:
                image(MiniMap.discoveredRoom, xPos, yPos, self.roomSize, self.roomSize)
                
            
            if room.visited:
                drawImg = None
                if room.type == Room.START:
                    drawImg = Room.startRoom
                elif room.type == Room.PUZZLE:
                    drawImg = Room.puzzleRoom
                elif room.type == Room.BATTLE:
                    drawImg = Room.battleRoom
                elif room.type == Room.EMPTY:
                    drawImg = Room.startRoom
                elif room.type == Room.END:
                    drawImg = Room.endRoom
                else:
                    drawImg = Room.startRoom
                
                
                image(drawImg, xPos, yPos, self.roomSize, self.roomSize)
                
                
                fill(50)
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
            if Room.currentRoom == room:
                image(MiniMap.currentRoomMarker, xPos, yPos, self.roomSize, self.roomSize)
                
            if room.discovered:
                fill(0)
                text(str(room.roomId) if room.roomId != -1 else "Start", xPos,yPos)
        imageMode(CORNER)
        textAlign(CORNER)
        fill(0)
        
        
        
def updateMiniMap():
        for direction in range(WEST, SOUTH+1):
            if Room.currentRoom.adjRooms[direction] != None and Room.currentRoom.doors[direction] != None:
                Room.currentRoom.adjRooms[direction].discovered = True
                
        
def initMiniMap():
    MiniMap.mapImage = loadImage("miniMap.png")
    MiniMap.discoveredRoom = loadImage("discoveredRoom.png")
    MiniMap.currentRoomMarker = loadImage("currentRoomMarker.png")
    MiniMap.mapBorder = [30, 30]
    