from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)

wall_image = games.load_image("images/wall.jpg", transparent = False)
games.screen.background = wall_image

won_message = games.Message(value = "You Won!", size = 100, color = color.red,
                             x = games.screen.width/2, y = games.screen.height/2, lifetime = 250, after_death = games.screen.quit)
#creates a message in the center of the screen for 250 frames, which after the program ends
#after death is a function to be runned afterobject destroy itself. default is none
#lifetime of 0  means never to destroy itself

games.screen.add(won_message)

games.screen.mainloop()