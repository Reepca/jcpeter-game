from room import Room
from sprite import Sprite
from util import x, y, NO_DIR, WEST, EAST, NORTH, SOUTH, directionSigns, boundBoxCheck
import __main__


class Character(Sprite):
    radius = 15
    # width, height - note, these are the dimensions for when it is facing
    # north/south.
    attackSize = 200, 100

    def __init__(self, initPos=(350, 350)):
        super(Character, self).__init__((initPos[x] - Character.radius,
                                         initPos[y] - Character.radius,
                                         initPos[x] + Character.radius,
                                         initPos[y] + Character.radius),
                                        self, location=initPos)
        self.velocity = 0, 0
        self.speed = .75
        self.damage = 5
        self.maxHealth = 100
        self.currentHealth = 100
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

        elif self.direction == NORTH:
            return (self.location[x] - Character.attackSize[x] / 2,
                    self.location[y] - Character.radius -
                    Character.attackSize[y],
                    self.location[x] + Character.attackSize[x] / 2,
                    self.location[y] - Character.radius)

    def isAttacking(self):
        return __main__.key_states.get(' ')

    def triggerDoorToggle(self):
        # Remember how you gave Sprite a boundingBox attribute?
        for door in Room.currentRoom.doors:
            if(boundBoxCheck(self.boundingBox, door.boundingBox)):
                door.toggleOpen()
                # if a room exists past the door you're trying to enter
                if Room.currentRoom.adjRooms[door.direction] != None:
                    oppositeDir = NO_DIR
                    oppositeDir = EAST if door.direction == WEST else oppositeDir
                    oppositeDir = NORTH if door.direction == SOUTH else oppositeDir
                    oppositeDir = SOUTH if door.direction == NORTH else oppositeDir
                    oppositeDir = WEST if door.direction == EAST else oppositeDir
                    print "triggerDoorToggle: (Room.currentRoom.adjRooms[door.direction])"
                    print Room.currentRoom.adjRooms[door.direction]
                    Room.currentRoom.adjRooms[door.direction].enter(oppositeDir)
                

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
        ellipse(x, y, 2*Character.radius, 2*Character.radius)
        # Drawing the attack box just to give us an idea of what it's like
        if self.isAttacking():
            left, top, right, bottom = self.attackBox()
            rect(left, top, right - left, bottom - top)

    def updatePosition(self, timePassed):
        dx = self.velocity[x] * timePassed
        dy = self.velocity[y] * timePassed
        left, top, right, bottom = self.boundingBox
        futureLeft = left + dx
        futureRight = right + dx
        futureTop = top + dy
        futureBottom = bottom + dy

        if boundBoxCheck(Room.currentRoom.boundingBox,
                         (futureLeft,
                          top,
                          futureRight,
                          bottom)):

            if boundBoxCheck(Room.currentRoom.boundingBox,
                             (futureLeft,
                              futureTop,
                              futureRight,
                              futureBottom)):
                self.move(dx, dy)
            else:
                self.move(dx, 0)
        elif boundBoxCheck(Room.currentRoom.boundingBox,
                           (left,
                            futureTop,
                            right,
                            futureBottom)):
            self.move(0, dy)


def updatePositions(timePassed):
    for sprite in Sprite.autoMoveSprites:
        sprite.updatePosition(timePassed)