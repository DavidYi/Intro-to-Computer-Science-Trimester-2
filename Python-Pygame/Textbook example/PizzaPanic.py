from livewires import games, color
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
    image = games.load_image("images/pan.bmp")
    
    def __init__(self):
        super(Pan, self).__init__(image = Pan.image, x = games.mouse.x, bottom = games.screen.height)
        #used the super function to make sure that the Sprite init method is called
        #then defined attribute, score, which is the player's score
        self.score = games.Text(value = 0, size = 25, color = color.black, top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)
        
    def update(self):
        self.x = games.mouse.x
        #allows the player to move the pan left and right
        
        if self.left < 0:
            self.left = 0
        #checks if its left edge is less than 0, meaning that part of the pan is beyond the left edge of the graphics window
        #if the left edge is set to 0, then the pan is displayed at the left edge of the window
        
        if self.right > games.screen.width:
            self.right = games.screen.width
        #checks if the right edge is bigger than the width of the screen, meaning part of the pan is beyond the right edge of the window
        #if the right edge is beyond it, thent it is displayed at the right edge of the window
            
        self.check_catch()
    
    def check_catch(self):
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            pizza.handle_caught()
        #for each object that overlaps the pan, the method increases the score by 10
        #then it ensure that the right edge of the text object for the score is always 10 pixels from the right edge of the screen

class Pizza(games.Sprite):
    image = games.load_image("images/pizza.bmp")
    speed = 1
    
    def __init__(self, x, y = 90):
        super(Pizza, self). __init__(image = Pizza.image, x = x, y = y, dy = Pizza.speed)
        #set the default value for y to 90, puts each new pizza right at the chef's chest level
    
    def update(self):
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()
        #checks if the bottom edge has reached screen bottom
    
    def handle_caught(self):
        self.destroy()
        #when the pizza collides with a pan, the pizza is considered "caught" and simply ceases to exist. destroy makes it disappear
    
    def end_game(self):
        end_message = games.Message(value = "Game Over", size = 90, color = color.red, x = games.screen.width/2,
                                     y = games.screen.height/2, lifetime = 5 * games.screen.fps, after_death = games.screen.quit)
        games.screen.add(end_message)
        #creates a message object that declares the game is over and then when the message disappears, the graphics window closes too.
        
class Chef(games.Sprite):
    image = games.load_image("images/chef.bmp")
    
    def __init__(self, y = 55, speed = 2, odds_change = 200):
        super(Chef, self).__init__(image = Chef.image, x = games.screen.width/2, y = y, dx = speed)
        self.odds_change = odds_change
        self.time_til_drop = 0
        #makes the sprite show in the screen, then creates two ints
        #odds_change mean that there is 1 out of 200 chance that every time the chef moves, he'll reverse direction
        #time_til_drop is int that represents the amount of time in mainloop cycles until the chef drops his next pizza
    
    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx
        #makes the chef change direction, meaning the pizza will be in a different "column"
        
        self.check_drop()
    
    def check_drop(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_pizza = Pizza(x = self.x)
            games.screen.add(new_pizza)
            
            self.time_til_drop = int(new_pizza.height * 1.3/ Pizza.speed) + 1
            #sets buffer to approx 30% of pizza height, regardless of pizza speed
        #makes a pizza where the chef is at

def main():
    wall_image = games.load_image("images/wall.jpg", transparent = False)
    games.screen.background = wall_image
    
    the_chef = Chef()
    games.screen.add(the_chef)
    
    the_pan = Pan()
    games.screen.add(the_pan)
    
    games.mouse.is_visible = False
    
    games.screen.event_grab = True
    games.screen.mainloop()

main()