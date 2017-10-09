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
    
    def __init__(self, capacity=30, startItems=[None for i in range(30)]):
        self.capacity = capacity
        self.inventoryMap = jArray()
        for i in range(capacity):
            self.inventoryMap[i] = (Inventory.initOffset[x] + Inventory.slotSize * (i % Inventory.colCount) + Inventory.betweenSlots[x] * (i % Inventory.colCount),
                                     Inventory.initOffset[y] + Inventory.slotSize * (i // Inventory.colCount) + Inventory.betweenSlots[y] * (i // Inventory.colCount))
        
    def draw(self, drawCoord=(0,0)):
        image(Inventory.inventoryImage, drawCoord[x], drawCoord[y])
        
        for i in range(self.capacity):
            fill(random.randint(0, 255))
            rect(drawCoord[x] + self.inventoryMap[i][x], drawCoord[y] + self.inventoryMap[i][y], Inventory.slotSize, Inventory.slotSize)
            fill(0)
            text(str(i), drawCoord[x] + self.inventoryMap[i][x], drawCoord[y] + self.inventoryMap[i][y])
        
def initInventory():
    Inventory.inventoryImage = loadImage("inventory.png")
    Inventory.initOffset[x] = 68
    Inventory.initOffset[y] = 38
    Inventory.betweenSlots[x] = 24
    Inventory.betweenSlots[y] = 7
    Inventory.slotSize = 49
    Inventory.rowCount = 5
    Inventory.colCount = 6