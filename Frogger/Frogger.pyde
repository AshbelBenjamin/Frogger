frog = {}
cars = []
jump = 10    # The distance the frog goes in one jump
livesLeft = 3

frogSize = 20
carWidth = 40
carHeight = 30

numCars = 5


def setup():
    """ Create the window and initialize the frog and car/s
    """
    global numCars,cars, frog   # This function will change these 
   
    size(500, 500)
    background(200, 255, 150)
    textSize(32)
   
    frog["x"] = width/2
    frog["y"] = 450
    
    for i in range (numCars):
        car = {}
        car["x"] = random(500 - carWidth)
        car["y"] = (i+1) * 70
        car["speed"]= random(1,5)
        cars.append(car)
        
def draw():
    global cars, frog, livesLeft   # This function may change these
   
    #  Repaint the background and the frog   
    background(200, 255, 150)   
    fill(60, 80, 80)
    rect(0, 0, width, 50)
    fill(255)
    text("Lives Left: " + str(livesLeft), 0, 40)
    drawFrog()
    
    if (livesLeft == 0):
        print("YOU LOST")
        fill(255,0,0)
        text("YOU LOST!",  150, 250 )
        return
    
    if (frog["y"] < 50):
        print("YOU WON")
        fill(random(255),random(255),random(255))
        text("YOU WON!",  150, 250 )
        return
   
    for i in range(numCars):
        moveCar(cars[i])
        drawCar(cars[i])
        if (collide(cars[i],frog)):
            #reset game
            reset()

def drawFrog():
    """ Draw the frog 
    """
    fill(0, 255, 0)
    ellipse(frog["x"], frog["y"], frogSize, frogSize)

#  Add your new functions here.
def collide(car, frog):
    if(car["y"] + carHeight) <= (frog["y"] - frogSize/2): # Top Side
        # print("Below Car")
        return False
    elif(car["y"] - carHeight) >= (frog["y"] + frogSize/2): # Bottom side
        # print("Above Car")
        return False
    elif(car["x"] + carWidth) <= (frog["x"] + frogSize/2): # Right side
        # print("Right of Car")
        return False
    elif(car["x"] - carWidth) >= (frog["x"] - frogSize/2): # Left side
        # print("Left of Car")
        return False
    else:
        # print("YOU DIED")
        return True



def drawCar(car):
    fill(255,0,0)
    rect(car["x"],car["y"],carWidth,carHeight)
    
def moveCar(car):
    car["x"] += car["speed"]
    if (car["x"] > width - carWidth) or (car["x"] < 1):
      car["speed"] *= -1
    
def keyPressed():
    if(key == CODED):
        if(keyCode == UP):
            # print("Up is Pressed")
            frog["y"] = frog["y"] - jump
        if(keyCode == DOWN):
            # print("Down is Pressed")
            frog["y"] = frog["y"] + jump
        if(keyCode == LEFT):
            # print("Left is Pressed")
            frog["x"] = frog["x"] - jump
        if(keyCode == RIGHT):
            # print("Right is Pressed")
            frog["x"] = frog["x"] + jump
            
            
def reset():
    global car, frog, livesLeft
    print ("YOU DIED")
    livesLeft = livesLeft -1
    frog["x"] = width/2
    frog["y"] = 450

    
