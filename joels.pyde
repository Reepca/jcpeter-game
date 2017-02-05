key_states = dict()

playerX = 0
playerY = 0
playerSpeed = 5

def setup():
    size(500, 500)

def draw():
    global playerX, playerY
    background(30, 50, 230)
    ellipse(playerX, playerY, 30, 30)
    if key_states.get(UP):
        playerY -= playerSpeed
    elif key_states.get(DOWN):
        playerY += playerSpeed
    if key_states.get(LEFT):
        playerX -= playerSpeed
    elif key_states.get(RIGHT):
        playerX += playerSpeed

def keyPressed():
    key_states[keyCode] = True

            
def keyReleased():
    key_states[keyCode] = False

def main():
    pass
    
main()