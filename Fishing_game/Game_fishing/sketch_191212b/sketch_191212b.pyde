
import os, random
path = os.getcwd()

class Game:
    def __init__(self):
        self.river = River()
        self.boat = Boat()
        self.fish = []
        self.fish_1 = []
        
    
        for i in range(6):
            self.fish.append(Fish(random.randint(0,2000)+1100,random.randint(350,600),loadImage(path + "/fish_image/"+str(random.randint(0,12))+".png")))
            
    def fish_eat(self):
        cnt = 0
        for fish in self.fish:
            m = int(self.boat.x)
            n = int(self.boat.m)
            i = int(fish.x)
            j = int(fish.y)
        
            print(m,n,i,j)
            distance = ((m - i)**2 + (n - j)**2)**0.5
            if distance <= 30:
                cnt += 1
                fish.vx = 0
                
                fish.x = m 
                fish.y = n
                if  n <= 210:
                    fish.x = (cnt*30)
                    fish.y = 0 
                    fish.r = 50
                    fish.v = 50
            
        
        
    
        
        
    def display(self):
        # self.river.move_river()
    
        self.boat.move_boat()
        for fish in self.fish:
            fish.move_fish()
        for fish_1 in self.fish_1:
            fish.move_fish()
        self.fish_eat()
            

    
        

class River:
    def __init__(self):
        self.x = 0
        self.y = 350
    
        self.img_num = 7
        # self.img_num1 = 7
        
 
        
    def move_river(self):
        
        # self.background_sound = player.loadFile(path + "/sounds/river_sound.mp3")
        # self.background_sound.rewind()
        # self.background_sound.play()
        image(loadImage(path + "/images/"+str(self.img_num)+".jpg"),self.x,self.y,1200,380)
        image(loadImage(path + "/images/"+str(self.img_num)+".jpg"),self.x+1100,self.y,1200,380)
        
        self.x -= 40
        if self.x <= -1100:
            self.x = 0
            # self.img_num = random.randint(0,7)
           
class Boat:
    def __init__(self):
        self.img = loadImage(path +"/images/fisherman.png")
        self.img1 = loadImage(path+"/images/hook.png")
        self.x = 400
        self.y = 210
        self.key_handler = {LEFT:False,RIGHT:True,UP:False,DOWN:False}
        self.m = 210
        self.vm = 10
        # self.n = 210
        # self.kill = False

    def move_boat(self):
    
        
        if self.key_handler[LEFT]:
            if self.x >= 5:
                image(self.img,self.x,self.y,150,150)
                image(self.img1,self.x-20,self.m+24,40,40)
                self.x -= 5
                if self.key_handler[DOWN]:
                    self.m += self.vm
                elif self.key_handler[UP] and self.m > 210:
                    self.m -= self.vm
                else:
                    self.m = self.m
            else:
                image(self.img,self.x,self.y,150,150)
                image(self.img1,self.x-20,self.m+24,40,40)
                if self.key_handler[DOWN]:
                    self.m += self.vm
                elif self.key_handler[UP] and self.m > 210:
                    self.m -= self.vm
                else:
                    self.m = self.m
                    
                # image(self.img,0,210,150,150)
            
            
            # self.y += random.randint(-3,3)
        elif self.key_handler[RIGHT]:
            if self.x <= 1000:
                image(self.img,self.x,self.y+7,150,150,503,0,0,537)
                
                image(self.img1,self.x+130,self.m+28,40,40,716,0,0,773)
                
                self.x += 5
                if self.key_handler[DOWN]:
                
                    self.m += self.vm
                elif self.key_handler[UP] and self.m > 210:
                    self.m -= self.vm
                else:
                    self.m = self.m
                
            else:
                image(self.img,self.x,self.y+7,150,150,503,0,0,537)
                image(self.img1,self.x+130,self.m+28,40,40,716,0,0,773)
                if self.key_handler[DOWN]:
                    self.m += self.vm
                elif self.key_handler[UP] and self.m > 210:
                    self.m -= self.vm
                else:
                    self.m = self.m
                
    
    
        
        # if self.kill == True:
        #     if self.n!= 500:
        #         fill(20,20,20)
        #         circle(self.m,self.n,20)
        #         self.n += 1
        # if self.key_handler[DOWN]:
        #     # fill(20,150,90)
        #     # circle(self.x,self.m,20)
        #     image(self.img1,self.x+130,self.m+28,40,40,716,0,0,773)
        #     self.m += 1
            # self.key_handler[DOWN]= True
   
            
            
            # self.x +=5
            # self.y += random.randint(-3,3)

class Fish:
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = img
        self.vx = random.randint(1,2)
        self.r = 0
        self.v = 0
    
    
        
        
    def fish_size(self):
        if self.y != 0:
            self.r = random.randint(45,65)
            self.v = random.randint(45,65)
            
    def move_fish(self): 
        self.fish_size()  
        image(self.img,self.x,self.y,self.r,self.v)
        self.x -= self.vx
        # self.hook.x = 400
        # self.hook.m = 500
        # image(self.image,self.mn,self.kl,150,150)
        # # if self.hook.x == self.mn and self.hook.m == self.kl:
        # #     image(self.image,self.mn,self.kl,150,150)
        # self.mn += 0
        # self.kl -= 0
            
    
    
        
        
        
                
        
        

game = Game()


def setup():
    size(1200, 700)
    background(255, 255, 255)
    
def draw():
    background(255, 255, 255)
    game.display()
    
def keyPressed():
    if keyCode == LEFT:
        game.boat.key_handler[LEFT] = True
    elif keyCode == RIGHT:
        game.boat.key_handler[RIGHT] = True
    elif keyCode == DOWN:
        game.boat.key_handler[DOWN] = True
    elif keyCode == UP:
        game.boat.key_handler[UP] = True
def keyReleased():
    if keyCode == LEFT:
        game.boat.key_handler[LEFT] = False
    if keyCode == RIGHT:
        game.boat.key_handler[RIGHT] = False
    if keyCode == DOWN:
        game.boat.key_handler[DOWN] = False
    if keyCode == UP:
        game.boat.key_handler[UP] = False
        
def mouseClicked():
    global game
    
    game.boat.kill = True
    
    
    




                
 
        
        
        
        
        

    
