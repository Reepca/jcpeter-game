
# This class is based heavily off of the example at
# https://processing.org/examples/animatedsprite.html
class Animation(object):
    
    def __init__(self, prefix, type, numFrames, displayRate=30):
        self.prefix = prefix
        self.type = type
        self.numFrames = numFrames
        self.displayRate = displayRate
        self.tempRate = 0
        self.currentFrame = 0
        self.time = millis()
        
        self.images = []
        
        for img in range(numFrames):
            tmp = loadImage(self.prefix + nf(img, 4) + self.type)
            self.images.append(tmp)
            
    def display(self, x, y):
        image(self.images[self.currentFrame], x, y)
        self.__updateFrame()
            
    def flipXDisplay(self, x, y):
        pushMatrix()
        scale(-1.0, 1.0)
        image(self.images[self.currentFrame], -self.images[self.currentFrame].width, 0);
        popMatrix
        self.__updateFrame()
            
    def __updateFrame(self):
        timeAtDisplay = millis()
        if timeAtDisplay - self.time > 1000 / self.displayRate:
            self.currentFrame = (self.currentFrame + 1) % self.numFrames
            self.time = timeAtDisplay
    
    def getWidth(self):
        return self.images[0].width
    
    def getHeight(self):
        return self.images[0].height
    
    def pause(self):
        self.tempRate = self.displayRate
        self.displayRate = 1
        
    def resume(self):
        self.displayRate = self.tempRate