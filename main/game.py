from dungeon import Dungeon
from jkey import Key
from room import Room, Door
from sprite import Sprite

class Game(object):
    victoryCount = 0
    def __init__(self, startSize=10, sizeScale=5, levelCount=4):
        self.startSize = startSize
        self.sizeScale = sizeScale
        self.levelCount = levelCount
        self.currentDungeon = Dungeon(startSize)
        Door.level = Game.victoryCount
        
    def pause():
        pass
        
    def nextLevel(self):
        if Game.victoryCount <= self.levelCount:
            self.clearClassVars()
            Door.level = Game.victoryCount
            self.currentDungeon = Dungeon(self.startSize + self.sizeScale * Game.victoryCount)
            print 'Current Level: ', Game.victoryCount
            
            
    def clearClassVars(self):
        Sprite.allSprites = []
        Sprite.autoMoveSprites = []
        Key.keyCount = 0
        Dungeon.floorKeys = []
        Room.currentRoom = None