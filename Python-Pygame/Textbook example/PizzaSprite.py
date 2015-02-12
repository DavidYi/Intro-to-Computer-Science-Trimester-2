from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

wall_image = games.load_image("images/wall.jpg", transparent = False)
games.screen.background = wall_image

pizza_image = games.load_image("images/pizza.bmp")
#loads a image and assigns it a variable
#the default value for transparent is true
#transparency makes the color at the upper left corner of the image is its transparent color.
pizza = games.Sprite(image = pizza_image, x = 320, y = 240)
#new sprite object is created and put in the middle of the screen

games.screen.add(pizza)
#add simply adds a sprite to the graphics screen
games.screen.mainloop()