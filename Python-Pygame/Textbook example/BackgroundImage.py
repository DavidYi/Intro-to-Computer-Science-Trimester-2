from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

wall_image = games.load_image("images/wall.jpg", transparent = False)
#loads the image stored in the file wall.jpg
games.screen.background = wall_image
#sets the background of the screen to the image object wall_image

games.screen.mainloop()