import math, random
from livewires import games, color
from random import randrange

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Wrapper(games.Sprite):
    #A sprite that wraps around the screen.
    def update(self):
        #wrap sprite around screen
        if self.top > games.screen.height:
            self.bottom = 0
            
        if self.bottom < 0:
            self.top = games.screen.height
        
        if self.left > games.screen.width:
            self.right = 0
        
        if self.right < 0:
            self.left = games.screen.width
    
    def die(self):
        #destroy self
        self.destroy()

class Collider(Wrapper):
    #a wrapper that can collide with another object
    def update(self):
        #checks for overlapping sprites
        super(Collider, self).update()
        #invokes supercalls's update method to keep the object on the screen
        
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()
    
    def die(self):
        #destroy self and leave explosion behind
        new_explosion = Explosion(x = self.x, y = self.y)
        games.screen.add(new_explosion)
        self.destroy()

class Explosion(games.Animation):
    #explosion animation and sound
    sound = games.load_sound("sounds/explosion.wav")
    images = ["images/explosion1.bmp", "images/explosion2.bmp", "images/explosion3.bmp", "images/explosion4.bmp", "images/explosion5.bmp",
                    "images/explosion6.bmp", "images/explosion7.bmp", "images/explosion8.bmp", "images/explosion9.bmp",]
    
    def __init__(self, x, y):
        super(Explosion, self).__init__(images = Explosion.images, x = x, y = y, repeat_interval = 4, n_repeats = 1, is_collideable = False)
        Explosion.sound.play()

class Ship(Collider):
    VELOCITY_MAX = 3
    #limit the maximum velocity of the player's ship
    
    image = games.load_image("images/ship.bmp")
    ROTATION_STEP = 3
    VELOCITY_STEP = .03
    #for altering the ship's velocity
    #higher number makes ship accelerate faster; lower would make the ship accelerate slower
    sound = games.load_sound("sounds/thrust.wav")
    #for thrusting sound of the ship
    MISSILE_DELAY = 25
    #represents delay a player must wait between missile firings
    
    def __init__(self, game, x, y):
        super(Ship, self).__init__(image = Ship.image, x = x, y = y)
        self.missile_wait = 0
        #used to count down the delay until the player can fire the next missile
        #initializes ship sprite
        self.game = game
        
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
            
            #cap the velocity in each direction           
            self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            #min returns the minimum of the two value and max returns the maximum of two values
        
        #fire missile if spacebar pressed and missile wait is over
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY
        
        #if waiting until the ship can fire next, decrease wait
        if self.missile_wait > 0:
            self.missile_wait -= 1 
        
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()
        
        super(Ship, self).update()
    
    def die(self):
        #destroy ship and end the game
        self.game.end()
        super(Ship, self).die()
            
class Missile(Collider):
    #a missile launced by the player's ship
    image = games.load_image("images/missile.bmp")
    sound = games.load_sound("sounds/missile.wav")
    
    BUFFER = 40
    #represents the distance from the ship that a new missile is created
    VELOCITY_FACTOR = 7
    #affects how fast the missile travels
    LIFETIME = 40
    #represents how long the missile exists before it disappears
    
    def __init__(self, ship_x, ship_y, ship_angle):
        #initializes missile sprite
        Missile.sound.play()
        #convert to radians
        angle = ship_angle * math.pi / 180
        
        #calculate missile's starting position
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)
        x = ship_x + buffer_x
        y = ship_y + buffer_y
        
        #calculate missile's velocity components
        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)
        
        #create the missile
        super(Missile, self).__init__(image = Missile.image, x = x, y = y, dx = dx, dy = dy)
        
        self.lifetime = Missile.LIFETIME
        #give missile object a lifetime attribute so that the object won't be around forever
        
    def update(self):
        games.Sprite.update(self)
        #if lifetime is up, destroy the missile
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()
            
        super(Missile, self).update()
        
class Asteroid(Wrapper):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL : games.load_image("images/asteroid_small.bmp"),
              MEDIUM : games.load_image("images/asteroid_med.bmp"),
              LARGE : games.load_image("images/asteroid_big.bmp")}
    #3 asteroid sizes, and cretae dictionary with the size and its corresponding image.
    SPEED = 2
    
    SPAWN = 2
    #number of new asteroids that an asteroids spawns when it's destroyed
    
    POINTS = 30
    #the constant act as a base number of points an asteroid is worth. THe actual point value will be modified according to the size.
    
    total = 0
    #to change levels, the program needs to know when all of the asteroid on the current lv is destroyed, so keep track for the total number
    
    def __init__(self, game, x, y, size):
        super(Asteroid, self).__init__(image = Asteroid.images[size], x = x, y = y,
                                       dx = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
                                       dy = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size)
        #when it is called all the required and other parameters are used to make a sprite. Also, passes a random value for an object velocity
        
        self.size = size
        
        Asteroid.total += 1
        
        self.game = game
        #reference to the game itself, so through the game, it can call a method of the game object
        
        
    def die(self):
        #if asteroid isn't small, replace with two smaller asteroids
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(game = self.game, x = self.x, y = self.y, size = self.size - 1)
                games.screen.add(new_asteroid)
            self.destroy()
                
        Asteroid.total -= 1
    
        self.game.score.value += int(Asteroid.POINTS / self.size)
        self.game.score.right = games.screen.width
        
        #if all the asteroids are gone advance to next level
        if Asteroid.total == 0:
            self.game.advance()
            
        super(Asteroid, self).die()

class Game(object):
    #the game itself
    def __init__(self):
        #initialize game object
        #set level
        self.level = 0
        #is attribute for teh current game level number
        
        #load sound for level advance
        self.sound = games.load_sound("sounds/level.wav")
        #sound is an attribute for the level advance sound effect
        
        #create score
        self.score = games.Text(value = 0, size = 30, color = color.white, top = 5, right = games.screen.width - 10, is_collideable = False)
        games.screen.add(self.score)
        #score is an attribute for the game score
        
        #create player's ship
        self.ship = Ship(game = self, x = games.screen.width/2, y = games.screen.height/2)
        games.screen.add(self.ship)
        #is an attribute for palyer's ship
    
    def play(self):
        #play game
        #begin theme music
        games.music.load("sounds/theme.mid")
        games.music.play(-1)
        
        #load and set background
        nebula_image = games.load_image("images/nebula.jpg")
        games.screen.background = nebula_image
        
        #advance to lv 1
        self.advance()
        
        #start play
        games.screen.mainloop()
        
    def advance(self):
        #advance to the next game lv
        self.level += 1
        
        #amount of space around ship to preserve when creating asteroids
        BUFFER= 150
        
        #create new asteroids
        for i in range(self.level):
            #calculate an x and y at least BUFFER distance from the ship
            
            #choose minimum distance along x-axis and y-axis
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min
            #minimum distance the new asteroid should be from the ship along the x and y axis
            
            #choose distance along x-axis and y- axis based on minimum distance
            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random. randrange(y_min, games.screen.height - y_min)
            #distance from the ship from the new asteroid and is randomly selected to ensure that the new asteroid will be at least the min distance
            
            #calculate location based on distance
            x = self.ship.x + x_distance
            y = self.ship.y + y_distance
            #coordinate for the asteroid 
            
            #wrap around screen, if necessary
            x %= games.screen.width
            y %= games.screen.height
            #make sure the asteroid won't put it off the screen by "wrapping it around" the screen with the modulus operator
            
            #create the asteroid
            new_asteroid = Asteroid(game = self, x = x, y = y, size = Asteroid.LARGE)
            games.screen.add(new_asteroid)
            
            #display lv #
            level_message = games.Message(value = "Level " + str(self.level), size = 40, color = color.yellow,
                                           x = games.screen.width/2, y = games.screen.width/10, lifetime = 3 * games.screen.fps, is_collideable = False)
            games.screen.add(level_message)
            
            #play new lv sound (except at first lv)
            if self.level > 1:
                self.sound.play()
            
    def end (self):
        #end of game
        #show game over for 5 sec
        end_message = games.Message(value = "Game Over", size = 90, color = color.red, 
                                    x = games.screen.width/2, y = games.screen.height/2, lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit, is_collideable = False)
        games.screen.add(end_message)

def main():
    astrocrash = Game()
    astrocrash.play()
    
main()