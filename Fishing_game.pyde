import os , random 
path = os.getcwd()



class Game:
    def __init__(self):
        
        self.river = River(0,350)
        
        
    def display(self):
        fill(140,140,140)
        self.river.move_river()
        
        
        
        

class River:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        # self.img_num = random.randint(0,7)
        self.img_num = 7
        # self.img_num1 = 7
        
       
    
        
        # self.img = loadImage(path + "/images/"+str(self.img_num)+".jpg")
        # self.img1 = loadImage(path + "/images/"+str(self.img_num1)+".jpg")
        
   
        
        
        
        
        
    def move_river(self):
        
        
        # image(self.img,self.x,self.y,1100,380)
        # image(self.img1,self.x+1100,self.y,1100,380)
        
        # image(self.img,self.x,self.y,1100,380)
        image(loadImage(path + "/images/"+str(self.img_num)+".jpg"),self.x,self.y,1100,380)
        image(loadImage(path + "/images/"+str(self.img_num)+".jpg"),self.x+1100,self.y,1100,380)
        
        self.x -=30
        if self.x <= -1100:
            self.x = 0
            self.img_num = random.randint(0,7)
            # self.img_num1 = random.randint(0,7)


    
    
    
    
    
    
    
        
        
        
    
    
    
    
    
class Fish:
    def __init__(self):
  
        self.vx = random.randint(1, 10)
        self.x1 = x1
        self.x2 = x2
    
    def update(self):
        self.gravity()
        
        if self.x < self.x1:
            self.direction = RIGHT
            self.vx *= -1
        elif self.x > self.x2:
            self.direction = LEFT
            self.vx *= -1
        
        if frameCount % 5 == 0:
            self.frame = (self.frame + 1) % self.slices
            
        self.y += self.vy
        self.x += self.vx
    
    
    
    
# class Boat:
    
    
    
        
        
        
        
        
        





game = Game()



def setup():
    size(1100,700)
    background(255,255,255)
    
def draw():
    background(115,205,55)
    game.display()
