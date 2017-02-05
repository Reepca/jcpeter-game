hit = False
class character():
    def __init__(self):
        self.x = 350
        self.y = 350
        self.speed = 10
        self.damage = 5

def setup():
    size(800,800)    
            
def draw():
    background(0)
    rect(character.x, character.y, 50, 50)
    if hit == True:
        rect(character.x + 50, character.y - 10, 50,70)
        rect(character.x + 25, character.y - 10, 25, 10)
        rect(character.x + 25, character.y + 50, 25, 10)
        
def keyPressed():
    global hit
    if(key == ' '):
        print(hit)
        hit = True
        
def keyReleased():
    global hit
    hit = False

def main():

    global character
    character = character()

main()