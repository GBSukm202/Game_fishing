import os, random
path = os.getcwd()

NUM_Col = 20
NUM_Row = 20

class Game(list): 
    def __init__(self):
        game = []
        for row in range (NUM_Row):
            row_list =[  ]
            for column in range (NUM_Col):
                row_list.append(' ')
        game.append(row_list)

class Snake:
    def __init__(self):
        self.snake = []
        self.snake.append(Head(11,10,30,30,0,0))
        for x in range(2):
            self.snake.append(Part(10,10,1,1,0,255))
    
    def appear(self):
        for x in self.snake:
            x.display()

class Head:
    def __init__(self,x,y,w,h,vx,vy):
        self.x = x
        self.y = y
        self.w = 30
        self.h = 30
        self.vx = vx
        self.vy = vy
        self.vx = 1
        self.X = self.x * 30
        self.Y = self.y * 30 
        self.status = True
    
    def display(self):
        if self.vx == 1:
            self.img = loadImage(path + "/images/head_left.png")
        if self.vx == -1:
            self.img = loadImage(path + "/images/head_left.png")
        if self.vy == 1:
            self.img = loadImage(path + "/images/head_up.png")
        if self.vy == -1:
            self.img = loadImage(path + "/images/head_up.png")
        self.x = self.x +self.vx
        self.y = self.y +self.vy
        self.X = self.x * 30
        self.Y = self.y * 30 
        image(self.img, self.X, self.Y, self.w, self.h)
        if self.X >600 or self.X <600 or self.Y >600 or self.Y <0:
            self.status = False


        
class Part:
    def __init__(self,x,y,e,vx,vy,c):
        self.x = x
        self.y = y
        self.e = e
        self.vx = vx
        self.vy = vy
        self.c = c 
        self.E = e*30
        self.n = 1
        
    def move(self): 
        if h.vx == 1:
            self.x = h.X
            self.y = h.y
        circle(self.x ,self.y, self.E)
    
    def display(self):
        circle(345,315,30)


class Food:
    def __init__(self):
        self.x = random.randint(0,20)
        self.y = random.randint(0,20)
        self.w = 30
        self.h = 30
        self.X = self.x * 30 
        self.Y = self.y * 30 
        if random.randint(0,2) == 1:            
            self.img = loadImage(path + "/images/apple.png")
        else:
            self.img = loadImage(path + "/images/banana.png")
    
    def show(self):
        image(self.img, self.X, self.Y, self.w, self.h)


def setup():
    g =Game()
    size(600,600)
    global s
    s = Snake()

def draw():
    if frameCount%12 == 0: 
        s.appear()
        # background(255) 
        # if h.status == False:
        #     fill(255,0,0)
        #     textSize(100)
        #     text("Game over", 100, 300)

      
    


def keyPressed():
    if keyCode == UP:
        if H.vy ==1 :
            pass
        else:
            H.vx = 0
            H.vy = -1
    if keyCode == DOWN:
        if H.vy == -1:
            pass 
        else:
            H.vx = 0
            H.vy = 1
    if keyCode == LEFT:
        if H.vx == 1:
            pass
        else:
            H.vx = -1
            H.vy = 0
    if keyCode == RIGHT:
        if H.vx == -1:
            pass
        else:
            H.vx = 1
            H.vy = 0



    
