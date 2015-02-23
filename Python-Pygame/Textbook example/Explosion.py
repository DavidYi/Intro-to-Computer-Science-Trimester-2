from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

nebula_image = games.load_image("images/nebula.jpg", transparent = False)
games.screen.background = nebula_image
    
explosion_files = ["images/explosion1.bmp", "images/explosion2.bmp", "images/explosion3.bmp", "images/explosion4.bmp", "images/explosion5.bmp",
                    "images/explosion6.bmp", "images/explosion7.bmp", "images/explosion8.bmp", "images/explosion9.bmp",]

explosion = games.Animation(images = explosion_files, x = games.screen.width/2, y = games.screen.height/2, n_repeats = 0, repeat_interval = 5)
games.screen.add(explosion)
#animation inherits all of sprite's attributes, properties and methods.
#n_repeats represents how many times the animation is displayed, again 0 means forever
#repeat interval represents the delay between successive images. The animation speed is dependent on this 

games.screen.mainloop()
