from sprite import Sprite
from room import Room

class Key(Sprite):
    keyImg = None
    keyCount = 0
    textHeight = 16
    def __init__(self, x, y, roomWithKey):
        # keyCount is the index of the room that the key unlocks
        # roomWithKey is the room that the key is stored in
        super(Key, self).__init__((x, y, x+Key.keyImg.width, y+Key.keyImg.height), self, location=(x,y))
        self.x = x
        self.y = y
        self.id = Key.keyCount
        self.roomWithKey = roomWithKey
        print "Key ", self.id, " in room ", roomWithKey
        Key.keyCount += 1
        
    def draw(self, x, y):
        # print Room.currentRoom
        if(Room.currentRoom == self.roomWithKey):
            fill(30)
            textSize(Key.textHeight)
            textAlign(CENTER)
            text("Key " + str(self.id), x+Key.keyImg.width/2, y-Key.textHeight)
            image(Key.keyImg, x, y)
        
def initKey():
    Key.keyImg = loadImage("key.png")