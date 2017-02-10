# Stuff that is used in scattered places throughout the project.

# Indexing into tuples
x = 0
y = 1

# Enums
NO_DIR = None
WEST = 0
EAST = 1
SOUTH = 2
NORTH = 3

# Useful for getting at the geometric meaning of these directions without a
# bunch of IFs
directionSigns = {WEST: -1, EAST: 1, SOUTH: 1,
                  NORTH: -1}