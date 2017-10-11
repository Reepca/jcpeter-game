import dungeon

class Game(object):
    victoryCount = 0
    def __init__(self, startSize=10, sizeScale=5, levelCount=4):
        self.startSize = startSize
        self.sizeScale = sizeScale
        self.levelCount = levelCount
        self.currentDungeon = dungeon.Dungeon(startSize)
        
    def pause():
        pass
        
    def nextLevel(self):
        self.currentDungeon.destroyDungeon()
        if Game.victoryCount <= self.levelCount:
            self.currentDungeon = dungeon.Dungeon(self.startSize + sizeScale * Game.victoryCount)