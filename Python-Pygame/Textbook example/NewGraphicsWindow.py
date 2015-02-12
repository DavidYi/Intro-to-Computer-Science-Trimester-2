from livewires import games

games.init (screen_width=640, screen_height=480, fps=50)
#games init() function  creates a new graphics screen

games.screen.mainloop()
#screen provides access to the graphics screen - the region on which graphics objects may exist, move, and interact
#starts the grapics screen mainloop