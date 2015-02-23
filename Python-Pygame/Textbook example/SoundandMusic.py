from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

missile_sound = games.load_sound("sounds/missile.wav")
#loads the sound file

games.music.load("sounds/theme.mid")
#loads the music file

choice = None
while choice != "0":
    
    print("""
    Sound and Music
    
    0 - Quit
    1 - Play missile sound
    2 - Loop Missile sound
    3 - Stop missile sound
    4 - Play theme music
    5 - Loop theme music
    6 - Stop theme music
    """)
    
    choice = input("Choice: ")
    print()
    
    #exit
    if choice == "0":
        print("Goodbye.")
    
    #play missile sound
    elif choice == "1":
       missile_sound.play()
       #how to play the loaded sound/ music
       #you can pass how many times to play the sound by passing a number to the method, which will play your number + 1 times.
       print("Playing missile sound") 
       
    #Loop missile sound
    elif choice == "2":
        loop = int(input("Loop how many extra times? (-1 = forever): "))
        missile_sound.play(loop)
        print("Looping missile sound.")
    
    #stop missile sound
    elif choice == "3":
        missile_sound.stop()
        #stops the music
        print("Stopping missile sound.")
    
    #plays theme music
    elif choice == "4":
        games.music.play()
        print("Playing theme music.")
        #this plays once since nothing is passed in the play parameters
        #plays the music that is currently loaded
    
    #Loops theme music
    elif choice == "5":
        loop = int(input("Loop how many extra times? (-1 = forever): "))
        games.music.play(loop)
        print("Looping theme music.")
        
    #Stops theme music
    elif choice == "6":
        games.music.stop()
        print("Stopping theme music.")
        
    #Unknown choice
    else:
        print("\nSorry, but", choice, "isn't a valid choice.")
        