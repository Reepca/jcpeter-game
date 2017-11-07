# Stuff that is used in scattered places throughout the project.

# Indexing into tuples
x = 0
y = 1

# Enums
NO_DIR = None
WEST = 0
NORTH = 1
EAST = 2
SOUTH = 3

# more Enums
IDLE = 0
WALKING = 1
ATTACKING = 2
JUMPING = 3


AJAR = True
CLOSED = False

# Useful for getting at the geometric meaning of these directions without a
# bunch of IFs
directionSigns = {WEST: -1, EAST: 1, SOUTH: 1,
                  NORTH: -1}


def boundBoxCheck((s1_left, s1_top, s1_right, s1_bot), (s2_left, s2_top,
                                                        s2_right, s2_bot)):
                # Our left is to the left of their right
        return (s1_left <= s2_right and
                # Our right is to the right of their left
                s1_right >= s2_left and
                # Our bottom is below their top (remember, in Processing top is
                # lower than bottom)
                s1_bot >= s2_top and
                # Our top is above their bottom (remember, in Processing bottom
                # is higher than top)
                s1_top <= s2_bot)

def inZone((s1_left, s1_top, s1_right, s1_bot), (s2_left, s2_top,
                                                        s2_right, s2_bot)):
    
    return (s2_left <= s1_left and
            s2_right >= s1_right and
            s2_top <= s1_top and
            s2_bot >= s1_bot)


def opposite(direction):
    oppositeDir = NO_DIR
    oppositeDir = EAST if direction == WEST else oppositeDir
    oppositeDir = NORTH if direction == SOUTH else oppositeDir
    oppositeDir = SOUTH if direction == NORTH else oppositeDir
    oppositeDir = WEST if direction == EAST else oppositeDir
    return oppositeDir

def median(lst):
    mid, remainder = divmod(len(lst), 2)
    if remainder == 0:
        return float(lst[mid-1] + lst[mid]) / 2
    else:
        return float(lst[mid])
    
    