class Sprite():
    """Anything in this class should be able to:
       - test for collision between itself and another Sprite
       - draw itself at its location
       - face a direction
       - have a location"""
    # Arbitrary enumeration
    WEST = 0
    EAST = 1
    SOUTH = 2
    NORTH = 3

    def __init__(self, boundingBox, drawer, direction=SOUTH, location=(0, 0)):
        """boundingBox is a tuple of the form left, top, right, bottom.
        IMPORTANT NOTE: top here means "Processing visual top", so it's
        actually numerically lower than bottom.

        drawer is an outsourcing of drawing capability to some other object,
        probably a PImage or something similar.

        direction is one of WEST, EAST, SOUTH, NORTH, or other useful ones we
        might want to add later.

        location is a tuple containing x and y position - it should be in the
        visual center of the object."""
        left, top, right, bottom = boundingBox
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.drawer = drawer
        self.direction = direction
        self.location = location

    def draw(self):
        self.drawer.draw(self.location[0], self.location[1])

    def checkCollision(self, otherSprite):
                # Our left is to the left of their right
        return (self.left <= otherSprite.right and
                # Our right is to the right of their left
                self.right >= otherSprite.left and
                # Our bottom is below their top (remember, in Processing top is
                # lower than bottom)
                self.bottom >= otherSprite.top and
                # Our top is above their bottom (remember, in Processing bottom
                # is higher than top)
                self.top <= otherSprite.bottom)
