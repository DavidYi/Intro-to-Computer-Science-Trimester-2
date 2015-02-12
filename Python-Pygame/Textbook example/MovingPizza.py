from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

wall_image = games.load_image("images/wall.jpg", transparent = False)
games.screen.background = wall_image

pizza_image = games.load_image("images/pizza.bmp")
the_pizza = games.Sprite(image = pizza_image, x = games.screen.width/2, y = games.screen.height/2, dx = 1, dy = 1)
#d stands for delta. dx changes the object's x-coordinate and dy changes the y-coordinate
#everytime the graphics window is updated by mainloop, the pizza's x-coordinate is increased by 1 and its y-coordinate is increased by 1
#moving the sprite right and down

games.screen.add(the_pizza)

games.screen.mainloop()