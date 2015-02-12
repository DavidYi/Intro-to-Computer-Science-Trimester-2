from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
    def update(self):
        #overwrites the object's update method
        self.x = games.mouse.x
        self.y = games.mouse.y
        #passes the object's x and y value to the mouse's x and y value
        
def main():
    wall_image = games.load_image("images/wall.jpg", transparent = False)
    games.screen.background = wall_image
    
    pan_image = games.load_image("images/pan.bmp")
    the_pan = Pan(image = pan_image, x = games.mouse.x, y = games.mouse.y)
    #the pan starts off at the mouse's coordinates

    games.screen.add(the_pan)
    
    games.mouse.is_visible = False
    #the mouse's pointer will not be visible
    
    games.screen.event_grab = True
    #grab all of the input to the graphics screen
    #means that all input will be focused on the graphics screen, means that the mouse won't leave the graphics window
    #to escape, press the esc button
    
    games.screen.mainloop()

main()