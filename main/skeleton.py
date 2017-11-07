from combatSprite import CombatSprite
from animation import Animation
from util import x, y, NO_DIR, WEST, EAST, NORTH, SOUTH, directionSigns, boundBoxCheck, opposite, inZone

class Skeleton(CombatSprite):
    
    # half of the bounding box (smaller than animation size)
    sizeX = 15
    sizeY = 25
    
    def __init__(self, initPos=(400, 400)):
        super(Skeleton, self).__init__((initPos[x] - Skeleton.sizeX,
                                         initPos[y] - Skeleton.sizeY,
                                         initPos[x] + Skeleton.sizeX,
                                         initPos[y] + skeleton.sizeY), #boundingBox
                                        self, # drawer
                                        initPos, #location
                                        (0,0), #velocity
                                        .15, #speed
                                        5, #damage
                                        30, #maxHealth
                                        30, #currentHealth
                                        False) #moving
        

    def draw(self, ):
        