from room import Room
from room import Door
from sprite import Sprite
from animation import Animation
from util import x, y, NO_DIR, WEST, EAST, NORTH, SOUTH, directionSigns, boundBoxCheck, opposite, inZone
import __main__


class Character(Sprite):
    
    playerAniPrefix = 'player'
    playerAniType = '.png'
    playerNumFrames = 2
    
    playerWalkPrefix = 'playerWalk'
    playerWalkType = '.png'
    playerWalkNumFrames = 7
    
    playerAttackPrefix = 'playerAttack'
    playerAttackType = '.png'
    playerAttackNumFrames = 0
    
    playerJumpPrefix = 'playerJump'
    playerJumpType = '.png'
    playerJumpNumFrames = 0
    
    bboxLeniency = 15
    radius = 25
    # width, height - note, these are the dimensions for when it is facing
    # north/south.
    attackSize = 200, 100

    IDLE = 0
    WALKING = 1
    ATTACKING = 2
    JUMPING = 3
    

    def __init__(self, initPos=(350, 350)):
        super(Character, self).__init__((initPos[x] - Character.radius,
                                         initPos[y] - Character.radius,
                                         initPos[x] + Character.radius,
                                         initPos[y] + Character.radius),
                                        self, location=initPos)
        
        self.velocity = 0, 0
        self.speed = .45
        self.damage = 5
        self.maxHealth = 100
        self.currentHealth = 100
        self.moving = False
        self.playerAni = Animation(Character.playerAniPrefix,
                                   Character.playerAniType,
                                   Character.playerNumFrames,
                                   6)
        self.playerWalkAni = Animation(Character.playerWalkPrefix,
                                       Character.playerWalkType,
                                       Character.playerWalkNumFrames
                                       )
        self.playerAttackAni = Animation(Character.playerAttackPrefix,
                                         Character.playerAttackType,
                                         Character.playerAttackNumFrames,
                                         10)
        self.playerJumpAni = Animation(Character.playerJumpPrefix,
                                       Character.playerJumpType,
                                       Character.playerJumpNumFrames,
                                       10)
        
        self.animations = [self.playerAni, self.playerWalkAni, self.playerAttackAni, self.playerJumpAni]
        Sprite.autoMoveSprites.append(self)

    def attackBox(self):
        """Gives the sides of the rectangle that is the attack box... in the
        same form as the boundingBox used by Sprite - that is, left, top,
        right, bottom"""
        if self.direction == WEST:
            return (self.location[x] - Character.radius -
                    Character.attackSize[y],
                    self.location[y] - Character.attackSize[x] / 2,
                    self.location[x] - Character.radius,
                    self.location[y] + Character.attackSize[x] / 2,)
            
        elif self.direction == NORTH:
            return (self.location[x] - Character.attackSize[x] / 2,
                    self.location[y] - Character.radius -
                    Character.attackSize[y],
                    self.location[x] + Character.attackSize[x] / 2,
                    self.location[y] - Character.radius)
            
        elif self.direction == EAST:
            return (self.location[x] + Character.radius,
                    self.location[y] - Character.attackSize[x] / 2,
                    self.location[x] + Character.radius +
                    Character.attackSize[y],
                    self.location[y] + Character.attackSize[x] / 2)

        elif self.direction == SOUTH:
            return (self.location[x] - Character.attackSize[x] / 2,
                    self.location[y] + Character.radius,
                    self.location[x] + Character.attackSize[x] / 2,
                    self.location[y] + Character.radius +
                    Character.attackSize[y])

        

    def isAttacking(self):
        return __main__.key_states.get(' ')

    def triggerDoorToggle(self):
        # Remember how you gave Sprite a boundingBox attribute?
        for door in Room.currentRoom.doors:
            
            if(boundBoxCheck(self.boundingBox, door.boundingBox)):
                print door
                door.toggleOpen()
                # if a room exists past the door you're trying to enter
                if Room.currentRoom.adjRooms[door.direction] != None:
                    Room.currentRoom.adjRooms[door.direction].enter(opposite(door.direction))
                    
                    # adjust player position so they are by the door they just opened
                    print "currentRoom: ", Room.currentRoom
                    print "Door Direction: ", door.direction
                    if door.direction == EAST:
                        self.move(-self.location[x] + Door.westDoorOpen.width, 0)
                    elif door.direction == SOUTH:
                        self.move(0, -self.location[y] + Door.northDoorOpen.height)
                    elif door.direction == NORTH:
                        self.move(0, -self.location[y] + height - Door.southDoorOpen.height)
                    elif door.direction == WEST:
                        self.move(-self.location[x] + width - Door.eastDoorOpen.width, 0) 
                return

    def setWalkY(self, flag):
        if flag is None:
            self.velocity = self.velocity[x], 0
        else:
            self.velocity = self.velocity[x], directionSigns[flag] * self.speed
            self.direction = flag

    def setWalkX(self, flag):
        if flag is None:
            self.velocity = 0, self.velocity[y]
        else:
            self.velocity = directionSigns[flag] * self.speed, self.velocity[y]
            self.direction = flag

    def draw(self, x, y):
        # these commented out lines draw the bounding box of the character.
        #left, top, right, bottom = self.boundingBox
        #rect(left, top, 2*Character.radius, 2*Character.radius)
        
        
        if not self.moving:
            print "Not walking"
            self.playerAni.display(x-Character.radius, y-Character.radius)
            
            
        else:
            print "Walking"
            self.playerWalkAni.display(x-Character.radius, y-Character.radius)
            

            
            
        # Drawing the attack box just to give us an idea of what it's like
        if self.isAttacking():
            left, top, right, bottom = self.attackBox()

    def updatePosition(self, timePassed):
        dx = self.velocity[x] * timePassed
        dy = self.velocity[y] * timePassed
        left, top, right, bottom = self.boundingBox
        futureLeft = left + dx
        futureRight = right + dx
        futureTop = top + dy
        futureBottom = bottom + dy
        if abs(dy) > 0 or abs(dx) > 0:
            self.moving = True
        else:
            self.moving = False
            
        if inZone((futureLeft+Character.bboxLeniency,
                   top+Character.bboxLeniency,
                   futureRight-Character.bboxLeniency,
                   bottom-Character.bboxLeniency), Room.currentRoom.boundingBox):
            if inZone((futureLeft+Character.bboxLeniency, 
                       futureTop+Character.bboxLeniency,
                       futureRight-Character.bboxLeniency, 
                       futureBottom-Character.bboxLeniency), Room.currentRoom.boundingBox):
                self.move(dx, dy)
            else:
                self.move(dx, 0)
        elif inZone((left+Character.bboxLeniency,
                     futureTop+Character.bboxLeniency,
                     right-Character.bboxLeniency,
                     futureBottom-Character.bboxLeniency), Room.currentRoom.boundingBox):
            self.move(0, dy)
        

def updatePositions(timePassed):
    for sprite in Sprite.autoMoveSprites:
        sprite.updatePosition(timePassed)