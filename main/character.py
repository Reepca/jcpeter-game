from room import Room
from room import Door
from combatSprite import CombatSprite
from animation import Animation
from inventory import Inventory
from dungeon import Dungeon
from game import Game
from util import x, y, NO_DIR, WEST, EAST, NORTH, SOUTH, directionSigns, boundBoxCheck, opposite, inZone, IDLE, WALKING, ATTACKING, JUMPING
import miniMap
import __main__


class Character(CombatSprite):
    
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
    

    def __init__(self, initPos=(400, 400)):
        
        super(Character, self).__init__((initPos[x] - Character.sizeX,
                                         initPos[y] - Character.sizeY,
                                         initPos[x] + Character.sizeX,
                                         initPos[y] + Character.sizeY), #boundingBox
                                        self, # drawer
                                        initPos, #location
                                        (0,0), #velocity
                                        .45, #speed
                                        5, #damage
                                        100, #maxHealth
                                        100, #currentHealth
                                        False) #moving

        self.inventory = Inventory()
        self.openInventory = False
        self.openMiniMap = False
        
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
        self.currentAnimation = self.animations[IDLE]
        Room.currentRoom.spritesInRoom.append(self)
        
        
    def teleportTo(self, location):
        self.location = location


    def toggleInventory(self):
        self.openInventory = not self.openInventory


    def toggleMiniMap(self):
        self.openMiniMap = not self.openMiniMap
        
        
    def isAttacking(self):
        return __main__.key_states.get(' ')


    def triggerDoorToggle(self):
        # Remember how you gave Sprite a boundingBox attribute?
        for door in Room.currentRoom.doors:
            if door:        
                if(boundBoxCheck(self.boundingBox, door.boundingBox)):
                    # if a room exists past the door you're trying to enter
                    roomPastDoor = Room.currentRoom.adjRooms[door.direction]
                    if roomPastDoor != None and (roomPastDoor.rightKey is None or self.inventory.contains(roomPastDoor.rightKey) or roomPastDoor.roomId < 0 or not roomPastDoor.locked):
                        door.toggleOpen()
                        
                        Room.currentRoom.spritesInRoom.remove(self)
                        Room.currentRoom.adjRooms[door.direction].enter(opposite(door.direction))
                        Room.currentRoom.spritesInRoom.append(self)
                        
                        __main__.updateGameInfo()
                        if roomPastDoor.rightKey is None or self.inventory.contains(roomPastDoor.rightKey):
                            self.inventory.drop(roomPastDoor.rightKey)
                        miniMap.updateMiniMap()
                        
                        # current win condition is entering the last room
                        if Room.currentRoom.type == Room.END and __main__.ourGame.levelCount > Game.victoryCount:
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
            self.currentAnimation = self.animations[IDLE]
        else:
            self.currentAnimation = self.animations[WALKING]

        # Drawing the attack box just to give us an idea of what it's like
        if self.isAttacking():
            left, top, right, bottom = self.attackBox()
            
        if self.openInventory:
            if __main__.key_states.get('m') or __main__.key_states.get('M'):
                __main__.ourGame.currentDungeon.miniMap.draw()
                self.openMiniMap = True
                self.openInventory = False
            else:
                self.inventory.draw((width/2 - Inventory.inventoryImage.width/2,
                                     height/2 - Inventory.inventoryImage.height/2))
            
            
        if self.openMiniMap:
            if __main__.key_states.get('e') or __main__.key_states.get('E'):
                self.inventory.draw((width/2 - Inventory.inventoryImage.width/2,
                                     height/2 - Inventory.inventoryImage.height/2))
                self.openInventory = True
                self.openMiniMap = False
            else:
                __main__.ourGame.currentDungeon.miniMap.draw()


    def movingChecks(self, timePassed):
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
            
        for jkey in Dungeon.floorKeys:
            if (not jkey.pickedUp and Room.currentRoom == jkey.roomWithKey and boundBoxCheck((futureLeft, futureTop, futureRight, futureBottom), jkey.boundingBox)):
                jkey.pickUp(self)