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
        self.img_num = 0
        # self.img = loadImage("C:/Users/310ch/Desktop/Project_CS/Fishing_game/images/4.jpg")
        self.img = loadImage(path + "/images/"+str(self.img_num)+".jpg")
        self.img_1 = loadImage(path + "/images/4.jpg")
        
        
        
        
        
    def move_river(self):
        
        image(self.img,self.x,self.y,1100,380)
        image(self.img_1,self.x+1100,self.y,1100,380)
        self.x -=20
        if self.x == -1100:
            self.x = 0
        
        
    
    
    
    
    
# class Fish:
    
    
    
    
# class Boat:
    
    
    
        
        
        
        
        
        





game = Game()



def setup():
    size(1100,700)
    background(255,255,255)
    
def draw():
    background(115,205,55)
    game.display()
