
# This class is based heavily off of the example at
# https://processing.org/examples/animatedsprite.html
class Animation(object):
    
    def __init__(self, prefix, type, numFrames, displayRate):
        self.prefix = prefix
        self.type = type
        self.numFrames = numFrames
        self.displayRate = displayRate
        self.currentFrame = 0
        self.time = millis()
        
        self.images = []
        
        for img in range(numFrames):
            tmp = loadImage(self.prefix + nf(img, 4) + self.type)
            self.images.append(tmp)
            
    def display(self, x, y):
        image(self.images[self.currentFrame], x, y)
        timeAtDisplay = millis()
        if timeAtDisplay - self.time > 1000 / self.displayRate:
            self.currentFrame = (self.currentFrame + 1) % self.numFrames
            self.time = timeAtDisplay
            
    def getWidth(self):
        return self.images[0].width
    
    def getHeight(self):
        return self.images[0].height