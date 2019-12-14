add_library('minim')
import os, random
path = os.getcwd()
player = Minim(this)



# Initialization of the Game 
class Game:
    def __init__(self):
        
        self.alive = True # Checking the player status 
    
        self.background_img = Background(0,0) # Initialization of the game background 
        self.river = River() #Initialization of the game river 
        self.boat = Boat()
        # self.hook = Hook()
        self.cnt = 0 
        self.fish = [] # Have fish from both direction
        self.fish_opposite = [] # Have fish from both direction
        self.score_fish = loadImage(path + "/fish_image_1/Fish_left/1.png") # Initialization of the fish image on upper right corner 
        self.final_fish = loadImage(path + "/fish_image/"+str(random.randint(0,5))+".jpg") # Display of the final image 
        self.snake = []
        self.snake_1 = []
    
        for i in range(7): # spawning the snake that can end the game 
            self.snake.append(Fish(random.randint(0,1000)+1100*i,random.randint(350,600),loadImage(path + "/snake_image/"+str(random.randint(2,3))+".png")))
            self.snake.append(Fish(random.randint(1000,6000)+1100*i,random.randint(350,600),loadImage(path + "/snake_image/"+str(random.randint(2,3))+".png")))
            self.snake_1.append(Fish(random.randint(-2000,0)+1100*i,random.randint(350,600),loadImage(path + "/snake_image/1.png")))
        
        
        
    
        for i in range(7): # Spawning the fish from both side 
            self.fish.append(Fish(random.randint(0,2000)+1100*random.randint(0,4),random.randint(350,600),loadImage(path + "/fish_image_1/Fish_right/"+str(random.randint(1,11))+".png")))
            self.fish.append(Fish(random.randint(2000,6000)+1100*random.randint(1,4),random.randint(350,600),loadImage(path + "/fish_image_1/Fish_right/more_fish/"+str(random.randint(1,5))+".jpg")))
    
            self.fish_opposite.append(Fish(random.randint(-2000,0)-100*random.randint(1,4),random.randint(350,600),loadImage(path + "/fish_image_1/Fish_left/"+str(random.randint(1,4))+".png")))
            
# function of snake (end game) 
    def snake_kill(self):
        for snake in self.snake:
            m = int(self.boat.a) # getting the coordinates of the hook 
            n = int(self.boat.b) # getting the coordinates of the hook 
       
            i = int(snake.x) # getting the coordinates of the snake
            j = int(snake.y) # getting the coordinates of the snake
        
            #Calcluation of distnace 
            distance_1 = (m - i)**2 
            distance_2 = (n - j)**2
            if distance_1 <= 400 and distance_2 <= 400:
                self.alive = False
                
                snake.vx = 0
                self.boat.vm = 0
                self.boat.boat_move = 0
                
# Display of the background when game ends         
    def final_background(self):
        self.background_sound = player.loadFile(path + "/sounds/game_end.mp3")
        self.background_sound.rewind()
        self.background_sound.play()
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
        
# Functon for pulling the fish up             
    def fish_eat(self):
        
        
        for fish in self.fish:
            m = int(self.boat.a) # getting the coordinates of the hook 
            n = int(self.boat.b) # getting the coordinates of the hook 
            i = int(fish.x)
            j = int(fish.y)
        
            # print(m,n,i,j)
            distance_1 = (m - i)**2 # Calculation of the distance between fish and hook 
            distance_2 = (n - j)**2
            if distance_1 <= 400 and distance_2 <= 400:
                '''self.background_sound = player.loadFile(path + "/sounds/fish_caught.mp3")
                self.background_sound.rewind()
                self.background_sound.play()'''
                
                
                fish.vx = 0 # Stop the fish from moving horizontally 
            
                fish.r = 20 # Pulling the fish up 
                fish.v = 20 # pulling the fish up 
                
                fish.x = self.boat.a
                fish.y = self.boat.b
                if  fish.y <= 250: # Moving up of the score 
                    self.background_sound = player.loadFile(path + "/sounds/fish_caught.mp3")
                    self.background_sound.rewind()
                    self.background_sound.play()
                    fish.x = (self.cnt*60)
                    fish.y = 0 
                    fish.r = 40
                    fish.v = 40
                    self.cnt += 1
        for fish in self.fish_opposite: # Same proces as the one above, but fish are spawned in differnt direction 
            m = int(self.boat.a)
            n = int(self.boat.b)
            i = int(fish.x)
            j = int(fish.y)
        
            # print(m,n,i,j)
            distance_1 = (m - i)**2 # Calculation of the distance between fish and hook
            distance_2 = (n - j)**2
            if distance_1 <= 400 and distance_2 <= 400:
                
                fish.vx = 0 # Stop the fish from moving horizontally 
                fish.r = 20 # Pulling the fish up 
                fish.v = 20 # pulling the fish up 
                
                fish.x = self.boat.a
                fish.y = self.boat.b
                if  fish.y <= 250:
                    self.background_sound = player.loadFile(path + "/sounds/fish_caught.mp3")
                    self.background_sound.rewind()
                    self.background_sound.play()
                    fish.x = (self.cnt*60)
                    fish.y = 0 
                    fish.r = 40
                    fish.v = 40
                    self.cnt += 1
        
# display of the game         
    def display(self):
        if self.alive == False:
            self.final_background() # display of the final background when game ends 
        else:
        
            self.background_img.show_background() # display of the upper part of the screen (sky) 
            self.river.move_river() # display of the lower part of the screen (ocean)
        
        
            self.boat.move_boat() # function that keeps the boat from moving 
            for fish in self.fish:
                fish.move_fish()
            for fish in self.fish_opposite:
                fish.move_fish_1()
            for snake in self.snake:
                snake.move_fish()
            for snake in self.snake_1:
                snake.move_fish_1()
            self.fish_eat() # function that makes the fish able to be pulled 
            fill(140,23,190)
            textSize(50)
            "{0} : {1}".format(image(self.score_fish,1000,40,100,100),text(str(self.cnt),1120,100))
            self.snake_kill()
# display of the lower part of the screen (ocean)        
class River:
    def __init__(self): # the coordinates for the image 
        self.x = 0
        self.y = 350
    
        self.img_num = 7 # Overall amount of image 
        # self.img_num1 = 7
        self.vx = 40 # The speed of the background's movement 
 
        
    def move_river(self):
        
        self.background_sound = player.loadFile(path + "/sounds/river_flow.mp3")
        self.background_sound.rewind()
        self.background_sound.play()
        image(loadImage(path + "/images/"+str(self.img_num)+".jpg"),self.x,self.y,1200,380) # display of the river by random selcetion 
        image(loadImage(path + "/images/"+str(self.img_num)+".jpg"),self.x+1100,self.y,1200,380)
        
        self.x -= self.vx
        if self.x <= -1100: # Make the river to continue to move
            self.x = 0
            self.img_num = random.randint(0,7)
# Loading of the boat, the boat include the fisherman, the hook, and the line that connects the hook to the boat            
class Boat:
    def __init__(self):
        self.img = loadImage(path +"/images/fisherman.png") # Image for the fisherman 
        self.img1 = loadImage(path+"/images/hook.png") # Image for the hook 
        # self.hook_line = loadImage(path+"/images/hook_line.png")
        self.hook_growth = 210 # the initial height of the hook on boat 
        self.hook_x = 10
        self.hm = 2
        self.x = 400
        self.y = 210
        self.key_handler = {LEFT:False,RIGHT:True,UP:False,DOWN:False} # handler that can be used to control the boat 
        self.m = 210
        self.vm = 10
        self.boat_move = 5
        self.a = 0
        self.b = 0
        
            

    def move_boat(self):
    
        if self.key_handler[LEFT]: # when the fisherman is facing left 
            if self.x >= 10:
                image(self.img,self.x,self.y,150,150) # the image of the hook when it is left
                line(self.x,234,self.x,self.hook_growth+35) # the line that connects the hook to the boat 
                stroke(204,153,0) # The color of the line 
                strokeWeight(2.5) # The width of the line 
                image(self.img1,self.x-20,self.m+24,40,40) 
                self.x -= self.boat_move # The movement of the hook 
                if self.key_handler[DOWN] and self.m < 600: # the function of the deploy button( down)  
                    self.m += self.vm
                    self.hook_growth += self.vm # the increase of the depth of the hook 
                elif self.key_handler[UP] and self.m > 210:
                    
                    self.m -= self.vm
                    self.hook_growth -= self.vm
                else:
                    self.m = self.m
            else: # If the fishermnan are near the edge of the screen, stop the movement of the fisherman 
                image(self.img,self.x,self.y,150,150) # the image of the boat 
                line(self.x,234,self.x,self.hook_growth+35) # the line that connects the hook to the boat 
                stroke(204,153,0)
                strokeWeight(2.5)
                image(self.img1,self.x-20,self.m+24,40,40) # the image of the hook 
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
        elif self.key_handler[RIGHT]:# Same as above, just different direction the fisherman is facing right 
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
                
            else:# to stop fisherman going away from screen 
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
                
            self.a = self.x+130 # the coordinate of the hook referencing to the coordinate of the boat (because there are white area on the side of the photo, we need to add 
                                #certain number to make it look real, same as below                                                                         
            self.b = self.m +28

class Background: 
    def __init__(self,x,y):
        self.x = x
        self.y = y 
        self.img_num = 1 # set the first image 
    
    def show_background(self): # loading of the river 
        image(loadImage(path + "/background/"+str(self.img_num)+".jpg"),self.x,self.y,1200,380)
        image(loadImage(path + "/background/"+str(self.img_num)+".jpg"),self.x+1200,self.y,1200,380)
        self.x -= 50 # movement of the river 
        if self.x <= -1200:
            self.x = 0
            self.img_num = random.randint(1,16) # Random display of imgae 


class Fish: # Spawning of the fish 
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = img
        self.vx = random.randint(1,6)
        self.r = 0
        self.v = 0
        
    def fish_size(self): 
        if self.y != 0:
            self.r = random.randint(45,65) #change the body size, to create illution of fish is alive
            self.v = random.randint(45,65)
            
    def move_fish(self):  # let the fish move 
        self.fish_size()  
        image(self.img,self.x,self.y,self.r,self.v)
        self.x -= self.vx 
    def move_fish_1(self): 
        self.fish_size()  
        image(self.img,self.x,self.y,self.r,self.v) # display of the snake 
        self.x += self.vx 

game = Game()


def setup():
    size(1200, 700)
    background(255, 255, 255)
    
def draw():
    background(255, 255, 255)
    game.display()
   
    # ALl the keys function here are refered back to each class  
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
        
def mouseClicked(): # to restart the game 
    global game
    if game.alive == False:
        game = Game()
    

    
    
    




                
 
        
        
        
        
        

    

                
 
        
        
        
        
        

    
