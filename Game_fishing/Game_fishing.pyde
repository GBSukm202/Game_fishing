add_library('minim')
import os, random
path = os.getcwd()
player = Minim(this)



class Game:
    def __init__(self):
    
    
    
    
        self.Background = Background(0,0)
        self.river = River(0,350) 
        # self.background_sound = player.loadFile(path + "/sounds/river_sound.mp3")
        # self.background_sound.rewind()
        # self.background_sound.play()
        self.boat = Boat()   
        self.hook = Hook(100,100,1080,1080)
        
    def display(self):
        self.Background.show_background()
        self.river.move_river()
        self.boat.move_boat()
        self.hook.move()

        
class Background: 
    def __init__(self,x,y):
        self.x = x
        self.y = y 
        self.img_num = 9  
    
    def show_background(self):
        image(loadImage(path + "/images/"+str(self.img_num)+".jpg"),self.x,self.y,1100,380)
        image(loadImage(path + "/images/"+str(self.img_num)+".jpg"),self.x+1100,self.y,1100,380)
        self.x -= 200
        if self.x <= -1100:
            self.x = 0
            self.img_num = random.randint(9,12)

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
            

class Hook:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = 1000
        self.h = 1080
        self.vy = 10     
        self.status = True
        self.img = loadImage(path + "/images/hook.jpg")
        
    
    def move(self):  
        self.y = self.y +self.vy
        if self.vy == 10:
            image(self.img, self.x, self.y,100,100)
        if self.y >3000:
            self.vy = -10
            self.status = False



class Part: # The tails of the snake 
    def __init__(self,x,y,e,c):
        self.x = x
        self.y = y
        self.e = e
        self.c = c
        
    def display(self):
        fill(80, 153, 32)
        circle(self.x*30, self.y*30, 30)
        
        
    
        
class Boat:
    def __init__(self):
        self.img = loadImage(path +"/images/fisherman.png")
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
    

    
        
                
                        
                                        
        
# class Fish:
    
#     def __init__(self):
        
        
        
#     def move_fish(self):
    
    


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
    if keyCode == DOWN:
        game.Hook.vy = 10
        
def keyReleased():
    if keyCode == LEFT:
        game.boat.key_handler[LEFT] = False
    # elif keyCode == RIGHT:
        # game.boat.key_handler[RIGHT] = False


                
 
        
        
        
        
        

    
