import tkinter

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        #makes the frame
        
    def create_widgets(self):
        row = 0
        tkinter.Label(self, text = "Choose a story.").grid(row = row, column = 0)
    
        row += 2
    
        self.stories = ["Surprise", "Tetris Master"]
        #Possible stories to choose from
        self.story = tkinter.StringVar()
        self.story.set(None)
        #makes self.story a string variable and sets its value to nothing
    
        for story in self.stories:
            tkinter.Radiobutton(self, text = story, variable = self.story, value = story).grid(row = row, column = 1, sticky = tkinter.W)
            row += 1 
        #makes radio button for each story
        
        tkinter.Button(self, text = "Continue", command = self.hide_children, bg = "Lime").grid(row = row, column = 2)
        tkinter.Button(self, text = "Quit", command = self.quit, bg = "red").grid(row = row, column = 4, columnspan = 2)
        #buttons that do exactly what it says
    
    def hide_children(self):
        #when you want to go edit the story
        for widget in self.winfo_children():
            widget.destroy()
        #gets rid of the widgets in the frame
        
        if self.story.get() == self.stories[0] or self.story.get() == self.stories[1]:
            #because it is from tkinter and a strvar, we have to use the get funnction or it will come out something liek this: PY_VAR0
            self.create_second_widgets()
        #This option is when the user picks a story
        else:
        #this is when the user does not pick a story
            tkinter.Label(self, text = "Please choose a story", bg = "Yellow", fg = "Crimson").grid(row = 1, column = 0, columnspan = 3)
            #adds a label
            self.create_widgets()
        
    def hide_children2(self):
        #when you want to go back to the story page
        for widget in self.winfo_children():
            widget.destroy()
        #gets rid of the widgets in the frame
        
        self.create_widgets()
        
    def create_second_widgets(self):
        tkinter.Label(self, text = "Enter information for a new story").grid(row = 0, column = 1, sticky = tkinter.W, columnspan = 3)
        tkinter.Button(self, text = "Back", command = self.hide_children2, bg = "DodgerBlue").grid(row = 0, column = 0, sticky = tkinter.W)
        #makes a label for directions and a button to go back to pick another story
        row = 1
        
        self.name_entry = ""
        self.verb_entry = ""
        self.object_entry = ""
        self.emotion_entry = ""
        #made this variable for the method check
        
        self.name_label = tkinter.Label(self, text = "Name: ")
        self.name_label.grid(row = row, column = 0, sticky = tkinter.W)
        #made it like this for the function check
        self.name_entry = tkinter.Entry(self)
        self.name_entry.grid(row = row, column = 1, sticky = tkinter.W)
        #gets what the user entered and uses it
        row += 1
        
        self.verb_label = tkinter.Label(self, text = "Verb: ")
        self.verb_label.grid(row = row, column = 0, sticky = tkinter.W)
        #for the function check
        self.verb_entry = tkinter.Entry(self)
        self.verb_entry.grid(row = row, column = 1, sticky = tkinter.W)
        row += 1
        
        self.object_label = tkinter.Label(self, text = "Object: ")
        self.object_label.grid(row = row, column = 0, sticky = tkinter.W)
        #for the function check
        self.object_entry = tkinter.Entry(self)
        self.object_entry.grid(row = row, column = 1, sticky = tkinter.W)
        row += 1
        
        self.emotion_label = tkinter.Label(self, text = "Emotion: ")
        self.emotion_label.grid(row = row, column = 0, sticky = tkinter.W)
        #for the function check
        self.emotion_entry = tkinter.Entry(self)
        self.emotion_entry.grid(row = row, column = 1, sticky = tkinter.W)
        row += 1
        
        self.adjective_label = tkinter.Label(self, text = "Adjective(s): ")
        self.adjective_label.grid(row = row, column = 0, sticky = tkinter.W)
        #for the function check
        
        self.is_delicious = tkinter.BooleanVar()
        #dont forget to use the get method
        tkinter.Checkbutton(self, text = "delicious", variable = self.is_delicious).grid(row = row, column = 1,sticky = tkinter.W)
            
        self.is_itchy = tkinter.BooleanVar()
        tkinter.Checkbutton(self, text = "itchy", variable = self.is_itchy).grid(row = row, column = 2, sticky = tkinter.W)
                                                                                 
        self.is_joyous = tkinter.BooleanVar()
        tkinter.Checkbutton(self, text = "joyous", variable = self.is_joyous).grid(row = row, column = 3, sticky = tkinter.W)
           
        self.is_electric = tkinter.BooleanVar()
        tkinter.Checkbutton(self, text = "electric", variable = self.is_electric).grid(row = row, column = 4, sticky = tkinter.W)
        row += 1
        
        tkinter.Button(self, text = "click for story", command = self.check, bg = "Lime").grid(row = row, column = 0, sticky = tkinter.W)
        #makes a button to submit the choices, but first it checks to see if they have the required fields
        
        row +=1
        
        self.story_txt = tkinter.Text(self, width = 75, height = 10, wrap = tkinter.WORD)
        self.story_txt.grid(row = row, column = 0, columnspan = 4)
        #makes a text box
        tkinter.Button(self, text = "Quit", command = self.quit, bg = "red").grid(row = row, column = 5)
        #this is a quit button
    
    def check(self):
        x = True
        error_msg = tkinter.Label(self, text = "Please input the required fields", fg = "Crimson", bg = "Yellow")
        error_msg.grid(row = 0, column = 3, columnspan = 3, sticky = tkinter.W)
        #creates an error message when the button is pressed, if the button is pressed and hte reuired fields is there then
        #it changes then quickly goes back   
        
        if self.emotion_entry.get() == "":
            #when it isn't chosen
            self.emotion_label["bg"] = "Crimson"
            x = False
        else:
            self.emotion_label["bg"] = self["bg"]
        
        if self.name_entry.get() == "":
            #when no one enters anything
            self.name_label["bg"] = "Crimson"
            x = False
        else:
            self.name_label["bg"] = self["bg"]
        
        if self.object_entry.get() == "":
            #when no one enters anything
            self.object_label["bg"] = "Crimson"
            x = False
        else:
            self.object_label["bg"] = self["bg"]
            
        if self.verb_entry.get() == "":
            self.verb_label["bg"] = "Crimson"
            x = False
        else:
            self.verb_label["bg"] = self["bg"]
            
        if (self.is_delicious.get() == False) and (self.is_electric.get() == False) and (self.is_itchy.get() == False) and (self.is_joyous.get() == False):
            #when the adjective wasn't changed
            self.adjective_label["bg"] = "Crimson"
            x = False
            #changes the background color
        else:
            self.adjective_label["bg"] = self["bg"]
            #changes label background to frame's color
            
        if x:
            self.tell_story()
            
            error_msg["bg"] = self["bg"]
            error_msg["fg"] = self["bg"]
            #changes the msg's background and font color into the background color of the frame
        else:
            error_msg["bg"] = "Yellow"
            error_msg["fg"] = "Crimson"
            #changes the label's background and font color to a different one

    def tell_story(self):
        name = self.name_entry.get()
        verb = self.verb_entry.get()
        objects = self.object_entry.get()
        emotion = self.emotion_entry.get()
        
        adjectives = ""
        #makes variable used in this method for story
        if self.is_delicious.get():
            adjectives += "delicious, "
            
        if self.is_itchy.get():
            adjectives += "itchy, "
            
        if self.is_joyous.get():
            adjectives += "joyous, "
            
        if self.is_electric.get():
            adjectives += "electric, "
        #makes adjective variable
        
        self.storydict = {}
        self.storydict["Surprise"] = "There once was a tiny little baby man named " + name + \
        " and there was a girl who loved him. In fact, this girl was so madly in love that she tried to " + verb +\
        " him. She succeeded terribly well that not only was " + name + " overcome with " + emotion + " and described it as " + adjectives +\
        " but also the girl found out that " + name + " was a SHE!!! The girl then, with a " + objects + ", became a boy." +\
        " Then the newly he found out that " + name + " was homosexual and cried himself to sleep."
        
        self.storydict["Tetris Master"] = "There once was a gamer named " + name + " and he loved to game. But most of all, he loved " +\
        "Tetris. It was fast-paced and required skillz. Now, " + name + " wanted to become the best tetris player in the world."+\
        " When " + name + " played with the worst tetris player, " + name + " lost. " + name + " was so overcome with " + emotion +\
        " that he decided to " + verb + " himself and he did exactly that with a " + objects + ". Afterwards, " + name + " came back describing it as " +\
        adjectives + "and he felt beautiful. Even after feeling that, " + name + " always remembered this moment in his heart and pieces of him chipped away as time passed..."
        #these are the stories
        
        self.story_txt.delete(0.0, tkinter.END)
        self.story_txt.insert(0.0, self.storydict[self.story.get()])
        #displays the story
    
root = tkinter.Tk()
root.title("Mad Lib")
frame = Application(root)
root.mainloop()
#displays it