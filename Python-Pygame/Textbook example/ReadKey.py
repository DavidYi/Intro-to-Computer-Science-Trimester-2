from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Ship(games.Sprite):
    def update(self):
        if games.keyboard.is_pressed(games.K_w):
            self.y -= 1
        
        if games.keyboard.is_pressed(games.K_s):
            self.y += 1
        
        if games.keyboard.is_pressed(games.K_a):
            self.x -= 1
        
        if games.keyboard.is_pressed(games.K_d):
            self.x += 1
        #this is how you reference the keys and use them to move the stuff
        #is pressed returns a boolean value and it is used to check if the certain button is pressed
    
def main():
    nebula_image = games.load_image("images/nebula.jpg", transparent = False)
    games.screen.background = nebula_image
    
    ship_image = games.load_image("images/ship.bmp")
    the_ship = Ship(image = ship_image, x = games.screen.width/2, y = games.screen.height/2)
    games.screen.add(the_ship)
    
    games.screen.mainloop()
    
main()