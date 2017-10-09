from sprite import Sprite
from room import Room
import inventory
from pickupable import Pickupable

class Key(Sprite, Pickupable):

    keyImg = None
    keyCount = 0
    textHeight = 14
    def __init__(self, x, y, roomWithKey):
        # keyCount is the index of the room that the key unlocks
        # roomWithKey is the room that the key is stored in
        super(Key, self).__init__((x, y, x+Key.keyImg.width, y+Key.keyImg.height), self, location=(x,y))
        self.pickedUp = False
        self.x = x
        self.y = y
        self.id = Key.keyCount
        self.roomWithKey = roomWithKey
        factor = inventory.getSlotSizeScale(Key.keyImg)
        self.inventoryImage = Key.keyImg.copy()
        self.inventoryImage.resize(int(Key.keyImg.width * factor), int(Key.keyImg.height * factor))
        print "Key ", self.id, " in room ", roomWithKey.roomId
        self.name = "Key " + str(self.id)
        Key.keyCount += 1
        
        
    def pickUp(self, character):
        self.pickedUp = True
        character.inventory.insert(self)
        
        
    def draw(self, x, y):
        # print Room.currentRoom
        if(Room.currentRoom == self.roomWithKey and not self.pickedUp):
            fill(255,0,0)
            myRect = self.getRect()
            #rect(myRect[0], myRect[1], myRect[2], myRect[3])
            fill(30)
            textSize(Key.textHeight)
            textAlign(CENTER)
            text("Key " + str(self.id), x+Key.keyImg.width/2, y-Key.textHeight)
            image(Key.keyImg, x, y)
            textAlign(LEFT)
        
def initKey():
    Key.keyImg = loadImage("key.png")