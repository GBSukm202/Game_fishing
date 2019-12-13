# add_library('minim')
import os, random
path = os.getcwd()
# player = Minim(this)




class Game:
    def __init__(self):
        
        self.alive = True
    
        self.background_img = Background(0,0)
        self.river = River()
        self.boat = Boat()
        # self.hook = Hook()
        self.cnt = 0 
        self.fish = []
        self.fish_opposite = []
        self.score_fish = loadImage(path + "/fish_image/"+str(random.randint(0,10))+".png")
        self.final_fish = loadImage(path + "/fish_image/final_background.jpg")
        self.snake = []
    
        for i in range(3):
            self.snake.append(Fish(random.randint(0,2000)+800,random.randint(350,600),loadImage(path + "/snake_image/"+str(random.randint(1,2))+".png")))
        
        
    
        for i in range(20):
            self.fish.append(Fish(random.randint(0,2000)+1100*random.randint(1,4),random.randint(350,600),loadImage(path + "/fish_image/"+str(random.randint(0,9))+".png")))
    
            self.fish_opposite.append(Fish(random.randint(-2000,0)-100*random.randint(1,4),random.randint(350,600),loadImage(path + "/fish_image/"+str(random.randint(0,9))+".png")))
            

    def snake_kill(self):
        for snake in self.snake:
            m = int(self.boat.a)
            n = int(self.boat.b)
       
            i = int(snake.x)
            j = int(snake.y)
        
        
            distance_1 = (m - i)**2 
            distance_2 = (n - j)**2
            if distance_1 <= 400 and distance_2 <= 400:
                self.alive = False
                
                snake.vx = 0
                self.boat.vm = 0
                self.boat.boat_move = 0
            
    def final_background(self):
        image(self.final_fish,0,0,1200,700)
    
        fill(190,10,100)
        textSize(100)
        text("Game Over", 320,200)
        fill(0,0,0)
        textSize(50)
        "{0} : {1}".format(image(self.score_fish,475,10,100,100),text(str(self.cnt),590,90))
        
        fill(120,26,180)
        textSize(70)
        text("Play Again", 440,350)
        

                
    def fish_eat(self):
        
        
        for fish in self.fish:
            m = int(self.boat.a)
            n = int(self.boat.b)
            i = int(fish.x)
            j = int(fish.y)
        
            # print(m,n,i,j)
            distance_1 = (m - i)**2 
            distance_2 = (n - j)**2
            if distance_1 <= 400 and distance_2 <= 400:
                
                
                fish.vx = 0
            
                fish.r = 20
                fish.v = 20
                
                fish.x = self.boat.a
                fish.y = self.boat.b
                if  fish.y <= 250:
                    fish.x = (self.cnt*60)
                    fish.y = 0 
                    fish.r = 40
                    fish.v = 40
                    self.cnt += 1
        for fish in self.fish_opposite:
            m = int(self.boat.a)
            n = int(self.boat.b)
            i = int(fish.x)
            j = int(fish.y)
        
            # print(m,n,i,j)
            distance_1 = (m - i)**2 
            distance_2 = (n - j)**2
            if distance_1 <= 400 and distance_2 <= 400:
                
                
                fish.vx = 0
                fish.r = 20
                fish.v = 20
                
                fish.x = self.boat.a
                fish.y = self.boat.b
                if  fish.y <= 250:
                    fish.x = (self.cnt*60)
                    fish.y = 0 
                    fish.r = 40
                    fish.v = 40
                    self.cnt += 1
        
        
    def display(self):
        if self.alive == False:
            self.final_background()
        else:
        
        
            self.background_img.show_background()
            self.river.move_river()
        
        
            self.boat.move_boat()
            for fish in self.fish:
                fish.move_fish()
            for fish in self.fish_opposite:
                fish.move_fish_1()
            for snake in self.snake:
                snake.move_fish()
            self.fish_eat()
            fill(140,23,190)
            textSize(50)
            "{0} : {1}".format(image(self.score_fish,1000,40,100,100),text(str(self.cnt),1120,100))
            self.snake_kill()
        
class River:
    def __init__(self):
        self.x = 0
        self.y = 350
    
        self.img_num = 7
        # self.img_num1 = 7
        self.vx = 40
 
        
    def move_river(self):
        
        # self.background_sound = player.loadFile(path + "/sounds/river_sound.mp3")
        # self.background_sound.rewind()
        # self.background_sound.play()
        image(loadImage(path + "/images/"+str(self.img_num)+".jpg"),self.x,self.y,1200,380)
        image(loadImage(path + "/images/"+str(self.img_num)+".jpg"),self.x+1100,self.y,1200,380)
        
        self.x -= self.vx
        if self.x <= -1100:
            self.x = 0
            self.img_num = random.randint(0,7)
           
class Boat:
    def __init__(self):
        self.img = loadImage(path +"/images/fisherman.png")
        self.img1 = loadImage(path+"/images/hook.png")
        self.hook_line = loadImage(path+"/images/hook_line.png")
        self.hook_growth = 210
        self.hook_x = 10
        self.hm = 2
        self.x = 400
        self.y = 210
        self.key_handler = {LEFT:False,RIGHT:True,UP:False,DOWN:False}
        self.m = 210
        self.vm = 10
        self.boat_move = 5
        self.a = 0
        self.b = 0
        
            

    def move_boat(self):
    
        if self.key_handler[LEFT]:
            if self.x >= 10:
                image(self.img,self.x,self.y,150,150)
                line(self.x,234,self.x,self.hook_growth+35)
                stroke(204,153,0)
                strokeWeight(2.5)
                image(self.img1,self.x-20,self.m+24,40,40)
                self.x -= self.boat_move
                if self.key_handler[DOWN] and self.m < 600:    
                    self.m += self.vm
                    self.hook_growth += self.vm
                elif self.key_handler[UP] and self.m > 210:
                    
                    self.m -= self.vm
                    self.hook_growth -= self.vm
                else:
                    self.m = self.m
            else:
                image(self.img,self.x,self.y,150,150)
                line(self.x,234,self.x,self.hook_growth+35)
                stroke(204,153,0)
                strokeWeight(2.5)
                image(self.img1,self.x-20,self.m+24,40,40)
                if self.key_handler[DOWN] and self.m < 600:
                    
                    # self.hook_x = 4
                    
                    self.m += self.vm
                    self.hook_growth += self.vm
                elif self.key_handler[UP] and self.m > 210:
                    # self.hook_x = 4
                    self.hook_growth -= self.vm
                    self.m -= self.vm
                else:
                    self.m = self.m

            self.a = self.x-20
            self.b = self.m +24
            
            # self.y += random.randint(-2,2)
        elif self.key_handler[RIGHT]:
            if self.x <= 1000:
                image(self.img,self.x,self.y+7,150,150,503,0,0,537)
                
                line(self.x+148,240,self.x+148,self.hook_growth+35)
                stroke(204,153,0)
                strokeWeight(2.5)
                image(self.img1,self.x+130,self.m+28,40,40,716,0,0,773)
                
                self.x += self.boat_move
                if self.key_handler[DOWN] and self.m < 600:
                
                    self.m += self.vm
                    # self.hook_x = 4
                    self.hook_growth += self.vm
                elif self.key_handler[UP] and self.m > 210:
                    self.m -= self.vm
                    # self.hook_x -= 4
                    self.hook_growth -= self.vm
                else:
                    self.m = self.m
                
            else:
                image(self.img,self.x,self.y+7,150,150,503,0,0,537)
                line(self.x+148,240,self.x+148,self.hook_growth+35)
                stroke(204,153,60)
                strokeWeight(2.5)
        
                image(self.img1,self.x+130,self.m+28,40,40,716,0,0,773)
            
                if self.key_handler[DOWN] and self.m < 600:
                    
                    self.hook_growth += self.vm
                    self.m += self.vm
                    
                
                    
                elif self.key_handler[UP] and self.m > 210:
                    self.m -= self.vm
            
                    self.hook_growth -= self.vm
                else:
                    self.m = self.m
                
            self.a = self.x+130
            self.b = self.m +28

class Background: 
    def __init__(self,x,y):
        self.x = x
        self.y = y 
        self.img_num = 1 
    
    def show_background(self):
        image(loadImage(path + "/background/"+str(self.img_num)+".jpg"),self.x,self.y,1200,380)
        image(loadImage(path + "/background/"+str(self.img_num)+".jpg"),self.x+1200,self.y,1200,380)
        self.x -= 50
        if self.x <= -1200:
            self.x = 0
            self.img_num = random.randint(1,14)


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
    def move_fish_1(self): 
        self.fish_size()  
        image(self.img,self.x,self.y,self.r,self.v,40,0,0,40)
        self.x += self.vx

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
    # if keyCode == RIGHT:
    #     game.boat.key_handler[RIGHT] = False
    if keyCode == DOWN:
        game.boat.key_handler[DOWN] = False
    if keyCode == UP:
        game.boat.key_handler[UP] = False
        
def mouseClicked():
    global game
    if game.alive == False:
        game = Game()
    

    
    
    




                
 
        
        
        
        
        

    

                
 
        
        
        
        
        

    
