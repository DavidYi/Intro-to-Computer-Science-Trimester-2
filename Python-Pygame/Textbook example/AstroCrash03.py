import math, random
from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Ship(games.Sprite):
    image = games.load_image("images/ship.bmp")
    ROTATION_STEP = 3
    VELOCITY_STEP = .03
    #for altering the ship's velocity
    #higher number makes ship accelerate faster; lower would make the ship accelerate slower
    sound = games.load_sound("sounds/thrust.wav")
    #for thrusting sound of the ship
       
    def update(self):
        #rotates based on keys pressed
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
    
        #plays the loaded sound    
        if games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
    
            #change velocity components based on ship's angle
            angle = self.angle * math.pi / 180 #convert to radians
            
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)
            #trig portion represents the percent of the thrust that should be applied to the ship's velocity in the y direction
    
        
        #wraps the ship around the screen
        if self.top > games.screen.height:
            self.bottom = 0
            
        if self.bottom < 0:
            self.top = games.screen.height
        
        if self.left > games.screen.width:
            self.right = 0
        
        if self.right < 0:
            self.left = games.screen.width
        
        

class Asteroid(games.Sprite):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL : games.load_image("images/asteroid_small.bmp"),
              MEDIUM : games.load_image("images/asteroid_med.bmp"),
              LARGE : games.load_image("images/asteroid_big.bmp")}
    #3 asteroid sizes, and cretae dictionary with the size and its corresponding image.
    SPEED = 2
    
    def __init__(self, x, y, size):
        super(Asteroid, self).__init__(image = Asteroid.images[size], x = x, y = y,
                                       dx = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
                                       dy = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size)
        #when it is called all the required and other parameters are used to make a sprite. Also, passes a random value for an object velocity
        
        self.size = size
    
    def update(self):
        #this keeps an asteroid in play by wrapping it around the screen
        if self.top > games.screen.height:
            self.bottom = 0
            
        if self.bottom < 0:
            self.top = games.screen.height
        
        if self.left > games.screen.width:
            self.right = 0
        
        if self.right < 0:
            self.left = games.screen.width
        
def main():
    #establish background
    nebula_image = games.load_image("images/nebula.jpg")
    games.screen.background = nebula_image
    
    #creates 8 asteroids
    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(x = x, y = y, size = size)
        games.screen.add(new_asteroid)
        
    #create the ship
    the_ship = Ship(image = Ship.image,  x = games.screen.width/2, y = games.screen.height/2)
    games.screen.add(the_ship)
    
    
    games.screen.mainloop()

main()