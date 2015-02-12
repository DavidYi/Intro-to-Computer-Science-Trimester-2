from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)

wall_image = games.load_image("images/wall.jpg", transparent = False)
games.screen.background = wall_image

score = games.Text(value = "1756521", size = 60, color = color.black, x = 550, y = 30)
#Text represents text on the graphics screen

games.screen.add(score)
#adds the score to the screen
#text is a subclass of sprite so it has all the properties of it and more
games.screen.mainloop()