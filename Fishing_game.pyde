add_library('minim')
import os, random
path = os.getcwd()
player = Minim(this)



class Game:
    def __init__(self):
    
    
    
    
        
        self.river = River(0,350) 
        # self.background_sound = player.loadFile(path + "/sounds/river_sound.mp3")
        # self.background_sound.rewind()
        # self.background_sound.play()
        self.boat = Boat()
        self.fish = []
        for i in range(10): 
            self.fish.append(Fish(random.randint(1100,4000),random.randint(350,700)))  
        
    def display(self):
        self.river.move_river()
        self.boat.move_boat()
        for fish in self.fish:
            fish.move_fish()
        
        
        
        
        
        

class River:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        # self.img_num = random.randint(0,7)
        self.img_num = 7
        # self.img_num1 = 7
        
 
        
    def move_river(self):
        
        self.background_sound = player.loadFile(path + "/sounds/river_sound.mp3")
        self.background_sound.rewind()
        self.background_sound.play()
        image(loadImage(path + "/images/"+str(self.img_num)+".jpg"),self.x,self.y,1100,380)
        image(loadImage(path + "/images/"+str(self.img_num)+".jpg"),self.x+1100,self.y,1100,380)
        
        self.x -= 100
        if self.x <= -1100:
            self.x = 0
            self.img_num = random.randint(0,7)
            

        
        
        
    
        
class Boat:
    def __init__(self):
        self.img = loadImage(path +"/images/fisherman.jpg")
        self.key_handler = {LEFT: False, RIGHT:True}
        self.vx = 10
        self.x = 400
        self.y = 200
        
    def move_boat(self):
        
        
        
    
        
        if self.key_handler[LEFT]:
            self.vx = -10
            self.direction = LEFT
            image(self.img,self.x,self.y,200,150)
        elif self.key_handler[RIGHT]:
            self.vx = 10
            self.direction = RIGHT
            image(self.img,self.x,self.y,300,250,800,0,0,800)
        else:
            self.vx = 0
            
        
        self.x += self.vx
    

    
        
                
                        
                                        
        
class Fish:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vx = random.randint(0,15)
        # self.vy = random.randint(-3,3)
        self.img = loadImage(path + "/fish_image/9.png")
        
        
        
    def move_fish(self):
        
        image(self.img, self.x,self.y,random.randint(45,70),random.randint(45,65))
        self.x -= self.vx
        # self.y -= self.vy
        
    
    


game = Game()

def setup():
    size(1100, 700)
    background(255, 255, 255)
    
def draw():
    background(255, 255, 255)
    game.display()

def keyPressed():
    if keyCode == LEFT:
        game.boat.key_handler[LEFT] = True
    # elif keyCode == RIGHT:
        # game.boat.key_handler[RIGHT] = True
    
        
def keyReleased():
    if keyCode == LEFT:
        game.boat.key_handler[LEFT] = False
    # elif keyCode == RIGHT:
        # game.boat.key_handler[RIGHT] = False
           
                
 
        
        
        
        
        

    
