from room import Room
from room import Door
from sprite import Sprite
from animation import Animation
from inventory import Inventory
from dungeon import Dungeon
from game import Game
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
    
    bboxLeniency = 10
    
    # these are actually half the width and height of our bounding box thing
    sizeY = 25 
    sizeX = 15
    # width, height - note, these are the dimensions for when it is facing
    # north/south.
    attackSize = 200, 100
    
    IDLE = 0
    WALKING = 1
    ATTACKING = 2
    JUMPING = 3

    def __init__(self, initPos=(350, 350)):
        super(Character, self).__init__((initPos[x] - Character.sizeX,
                                         initPos[y] - Character.sizeY,
                                         initPos[x] + Character.sizeX,
                                         initPos[y] + Character.sizeY),
                                        self, location=initPos)
        
        self.playerAni = Animation(Character.playerAniPrefix,
                                   Character.playerAniType,
                                   Character.playerNumFrames,
                                   10)
        self.velocity = 0, 0
        self.speed = .45
        self.damage = 5
        self.maxHealth = 100
        self.currentHealth = 100
        self.moving = False
        self.inventory = Inventory()
        self.openInventory = False
        
        # Adjust hitbox to fit animation size
        left, top, right, bottom = self.boundingBox
        self.boundingBox = (left + Character.sizeX/2, top, right + Character.sizeX/2, bottom)
        
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
        self.currentAnimation = self.animations[Character.IDLE]
        Sprite.autoMoveSprites.append(self)
        

    def toggleInventory(self):
        self.openInventory = not self.openInventory


    def attackBox(self):
        """Gives the sides of the rectangle that is the attack box... in the
        same form as the boundingBox used by Sprite - that is, left, top,
        right, bottom"""
        if self.direction == WEST:
            return (self.location[x] - Character.sizeX -
                    Character.attackSize[y],
                    self.location[y] - Character.attackSize[x] / 2,
                    self.location[x] - Character.sizeX,
                    self.location[y] + Character.attackSize[x] / 2,)
            
        elif self.direction == NORTH:
            return (self.location[x] - Character.attackSize[x] / 2,
                    self.location[y] - Character.sizeY -
                    Character.attackSize[y],
                    self.location[x] + Character.attackSize[x] / 2,
                    self.location[y] - Character.sizeY)
            
        elif self.direction == EAST:
            return (self.location[x] + Character.sizeX,
                    self.location[y] - Character.attackSize[x] / 2,
                    self.location[x] + Character.sizeX +
                    Character.attackSize[y],
                    self.location[y] + Character.attackSize[x] / 2)

        elif self.direction == SOUTH:
            return (self.location[x] - Character.attackSize[x] / 2,
                    self.location[y] + Character.sizeY,
                    self.location[x] + Character.attackSize[x] / 2,
                    self.location[y] + Character.sizeY +
                    Character.attackSize[y])

        

    def isAttacking(self):
        return __main__.key_states.get(' ')


    def triggerDoorToggle(self):
        # Remember how you gave Sprite a boundingBox attribute?
        for door in Room.currentRoom.doors:
            if door:        
                if(boundBoxCheck(self.boundingBox, door.boundingBox)):
                    # if a room exists past the door you're trying to enter
                    roomPastDoor = Room.currentRoom.adjRooms[door.direction]
                    if roomPastDoor != None and (roomPastDoor.rightKey is None or self.inventory.contains(roomPastDoor.rightKey) or roomPastDoor.roomId < 0):
                        door.toggleOpen()
                        Room.currentRoom.adjRooms[door.direction].enter(opposite(door.direction))
                        if Room.currentRoom.type == Room.END:
                            Game.victoryCount += 1
                        # adjust player position so they are by the door they just opened
                        print "currentRoom: ", Room.currentRoom
                        print "Door Direction: ", door.direction
                        if door.direction == EAST:
                            self.move(-self.location[x] + Door.westDoorOpen.width + self.currentAnimation.getWidth() / 2, 0)
                        elif door.direction == SOUTH:
                            self.move(0, -self.location[y] + Door.northDoorOpen.height + self.currentAnimation.getHeight() / 2)
                        elif door.direction == NORTH:
                            self.move(0, -self.location[y] + height - Door.southDoorOpen.height - self.currentAnimation.getHeight() / 2)
                        elif door.direction == WEST:
                            self.move(-self.location[x] + width - Door.eastDoorOpen.width - self.currentAnimation.getWidth() / 2, 0) 
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
        # these commented out lines draw the bounding box of the character..
        left, top, right, bottom = self.boundingBox
        #fill(0, 255, 0)
        #rect(left, top, 2*Character.sizeX, 2*Character.sizeY)
        
        if self.velocity[0] >= 0:
            self.currentAnimation.display(x - Character.sizeX, y - Character.sizeY)
        else:
            self.currentAnimation.flipXDisplay(x - Character.sizeX, y - Character.sizeY)
        
        if not self.moving:
            self.currentAnimation = self.animations[Character.IDLE]
        else:
                self.currentAnimation = self.animations[Character.WALKING]

        # Drawing the attack box just to give us an idea of what it's like
        if self.isAttacking():
            left, top, right, bottom = self.attackBox()
            
        if self.openInventory:
            self.inventory.draw((width/2 - Inventory.inventoryImage.width/2,
                                 height/2 - Inventory.inventoryImage.height/2))


    def updatePosition(self, timePassed):
        dx = self.velocity[x] * timePassed
        dy = self.velocity[y] * timePassed
        left, top, right, bottom = self.boundingBox
        left += Character.bboxLeniency
        right -= Character.bboxLeniency
        top += Character.bboxLeniency
        bottom -= Character.bboxLeniency
        futureLeft = left + dx
        futureRight = right + dx
        futureTop = top + dy
        futureBottom = bottom + dy
        if abs(dy) > 0 or abs(dx) > 0:
            self.moving = True
        else:
            self.moving = False
            
        for jkey in Dungeon.floorKeys:
            if (not jkey.pickedUp and Room.currentRoom == jkey.roomWithKey and boundBoxCheck((futureLeft, futureTop, futureRight, futureBottom), jkey.boundingBox)):
                jkey.pickUp(self)
                print "Picked up jkey ", jkey.id
            
            
        if inZone((futureLeft, top, futureRight, bottom), Room.currentRoom.boundingBox):
            if inZone((futureLeft, futureTop, futureRight, futureBottom), Room.currentRoom.boundingBox):
                self.move(dx, dy)
            else:
                self.move(dx, 0)
        elif inZone((left, futureTop, right, futureBottom), Room.currentRoom.boundingBox):
            self.move(0, dy)
            
        

def updatePositions(timePassed):
    for sprite in Sprite.autoMoveSprites:
        sprite.updatePosition(timePassed)