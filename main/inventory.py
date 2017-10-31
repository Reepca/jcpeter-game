from jArray import jArray
from util import x, y
import random

class Inventory(jArray):
    
    inventoryImage = None
    initOffset = [0, 0]
    betweenSlots = [0, 0]
    slotSize = 0
    rowCount = 0
    colCount = 0
    textHeight = 14
    
    def __init__(self, capacity=30, startItems=[None for i in range(30)]):
        super(Inventory, self).__init__(capacity)
        self.capacity = capacity
        self.inventoryMap = jArray()
        for i in range(capacity):
            self.inventoryMap[i] = (Inventory.initOffset[x] + Inventory.slotSize * (i % Inventory.colCount) + Inventory.betweenSlots[x] * (i % Inventory.colCount),
                                     Inventory.initOffset[y] + Inventory.slotSize * (i // Inventory.colCount) + Inventory.betweenSlots[y] * (i // Inventory.colCount))
        self.firstEmpty = 0
        self.fullInventory = False
        
        
    def insert(self, newThing):
        self.data[self.firstEmpty] = newThing
        successStatus = True
        try:
            self.firstEmpty = self.data.index(None)
        except ValueError:
            successStatus = False
            print "Can't insert item into inventory; Inventory is full"
            self.firstEmpty = -1
        self.updateFullStatus()
        print "added ", newThing
        return successStatus
        
        
    def drop(self, thing):
        try:
            self.firstEmpty = self.data.index(thing)
        except ValueError:
            print(thing, "not in inventory! Cannot drop!")
        self.data[self.firstEmpty] = None
        
        
    
    def contains(self, thing):
        print "Inventory has", thing.name, ":", True if self.data.count(thing) > 0 else False
        return True if self.data.count(thing) > 0 else False
    
        
    def updateFullStatus(self):
        self.fullInventory = True if self.firstEmpty >= self.capacity or self.firstEmpty < 0 else False
        
        
    def draw(self, drawCoord=(0,0)):
        image(Inventory.inventoryImage, drawCoord[x], drawCoord[y])
        textSize(Inventory.textHeight)
        imageMode(CENTER)
        for i in range(self.capacity):
            # silly, but this needs a property named "inventoryImage"
            if self.data[i] != None:
                image(self.data[i].inventoryImage, drawCoord[x] + self.inventoryMap[i][x] + Inventory.slotSize/2, drawCoord[y] + self.inventoryMap[i][y] + Inventory.slotSize/2)
                
                text(self.data[i].name, drawCoord[x] + self.inventoryMap[i][x], drawCoord[y] + self.inventoryMap[i][y])
            # put inventory slot number to left of slot
            text(str(i), drawCoord[x] + self.inventoryMap[i][x] - Inventory.betweenSlots[x]/2, drawCoord[y] + self.inventoryMap[i][y] + Inventory.slotSize/2)
        imageMode(CORNER)
        
            

def getSlotSizeScale(img):
    k = 1
    if(img.width > Inventory.slotSize and img.height > Inventory.slotSize):
        k = max(float(Inventory.slotSize) / float(img.width), float(Inventory.slotSize) / float(img.height))
    else:
        k = min(float(Inventory.slotSize) / float(img.width), float(Inventory.slotSize) / float(img.height))
    return k
        
        
def initInventory():
    Inventory.inventoryImage = loadImage("inventory.png")
    Inventory.initOffset[x] = 68
    Inventory.initOffset[y] = 38
    Inventory.betweenSlots[x] = 24
    Inventory.betweenSlots[y] = 7
    Inventory.slotSize = 49
    Inventory.rowCount = 5
    Inventory.colCount = 6