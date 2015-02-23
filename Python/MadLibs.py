import tkinter
#you need self for everything because, it becomes the master and you need it to put everything on the same frame

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        tkinter.Label(self, text = "Enter information for a new story").grid(row = 0, column = 0, sticky = tkinter.W)
        #makes a label for directions
        
        tkinter.Label(self, text = "Person: ").grid(row = 1, column = 0 , sticky = tkinter.W)
        self.person_entry = tkinter.Entry(self)
        self.person_entry.grid(row = 1, column = 1, sticky = tkinter.W)
        #makes a label for person and a place to enter it
        
        tkinter.Label(self, text = "Plural Noun: ").grid(row = 2, column = 0 , sticky = tkinter.W)
        self.noun_entry = tkinter.Entry(self)
        self.noun_entry.grid(row = 2, column = 1, sticky = tkinter.W)
        #makes a label for noun and a place to enter it
        
        tkinter.Label(self, text = "Verb: ").grid(row = 3, column = 0 , sticky = tkinter.W)
        self.verb_entry = tkinter.Entry(self)
        self.verb_entry.grid(row = 3, column = 1, sticky = tkinter.W)
        #makes a label for verb and a place to enter it
        
        tkinter.Label(self, text = "Adjective(s): ").grid(row = 4, column = 0 , sticky = tkinter.W)
        #makes a label for adjectives
        
        self.is_itchy = tkinter.BooleanVar()
        tkinter.Checkbutton(self, text = "itchy", variable = self.is_itchy).grid(row = 4, column = 1, sticky = tkinter.W)
        
        self.is_joyous = tkinter.BooleanVar()
        tkinter.Checkbutton(self, text = "joyous", variable = self.is_joyous).grid(row = 4, column = 2, sticky = tkinter.W)
        
        self.is_electric = tkinter.BooleanVar()
        tkinter.Checkbutton(self, text = "electric", variable = self.is_electric).grid(row = 4, column = 3, sticky = tkinter.W)
        #makes choices for the label adjectives and assigns variable to a boolean variable
        
        
        tkinter.Label(self, text = "Body Part: ").grid(row = 5, column =0, sticky = tkinter.W)
        
        self.body_part = tkinter.StringVar()
        self.body_part.set(None)
        #makes a label and some variables
        #assigns the variable to a string variable
        
        body_parts = ["bellybutton", "big toe", "medulla oblongata"]
        column = 1
        for part in body_parts:
            tkinter.Radiobutton(self, text = part, variable = self.body_part,
                         value = part).grid(row = 5, column = column, sticky = tkinter.W)
            column += 1
        #another way to go and make multiple radio buttons and is much cleaner
        
        tkinter.Button(self, text = "click for story", command = self.tell_story).grid(row = 6, column = 0, sticky = tkinter.W)
        #makes a button to submit the choices
        
        self.story_txt = tkinter.Text(self, width = 75, height = 10, wrap = tkinter.WORD)
        self.story_txt.grid(row = 7, column = 0, columnspan = 4)
        #makes a text box
    
    def tell_story(self):
        person = self.person_entry.get()
        noun = self.noun_entry.get()
        verb = self.verb_entry.get()
        #gets all the variable value, you need .get()
        adjectives = ""
        #makes variable used in this method for story
        
        if self.is_itchy.get():
            #since self.is_itchy is a boolean variable, if it is true it adds the adjective to the variable
            adjectives += "itchy, "
            
        if self.is_joyous.get():
            adjectives += "joyous, "
            
        if self.is_electric.get():
            adjectives += "electric, "
        #makes adjective variable
        
        body_parts = self.body_part.get()
        
        #making the story
        story = "The famous explorer "
        story += person
        story += " had nearly given up a life-long quest to find The Lost City of "
        story += noun.title()
        story += " when one day, the "
        story += noun
        story += " found "
        story += person + "."
        story += "A strong, "
        story += adjectives
        story += " peculiar feeling overwhelmed the explorer. "
        story += "After all this time, the quest was finally over. A tear came to "
        story += person + "'s "
        story += body_parts + ". "
        story += "And then, the "
        story += noun
        story += " promptly devoured"
        story += person +". "
        story += "The moral of the story? Be careful what you "
        story += verb
        story += " for."
        
        self.story_txt.delete(0.0, tkinter.END)
        self.story_txt.insert(0.0, story)
        #displays the story
        #0.0 is the start point. coloumn 0 and row 0 of self.story_txt

root = tkinter.Tk()
root.title("Mad Lib")
frame = Application(root)
root.mainloop()
