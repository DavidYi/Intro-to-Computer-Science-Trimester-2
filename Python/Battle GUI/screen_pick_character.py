import tkinter
from Tooltip import Tooltip

class Screen_character_selector (tkinter.Frame):
    def __init__ (self, master, char_list, call_on_selected, choice):
        super(Screen_character_selector, self).__init__(master)
        
        # Save the list of characters 
        self.char_list = char_list
        
        self.choice = choice
        
        # Save the method reference to which we return control after the player hits "Next"
        self.call_on_selected = call_on_selected
        
        self.grid()
        self.create_widgets()
        
    def create_widgets (self):
        '''
        This method creates all of the widgets character selector page.
        
        The radio buttons on this page must use the variable "self.character".  
        The values of the radio buttons must be a number equally the position of the character in the list. 
        For example, if the characters listed are Troll, Elf, Human, and Dwarf.  self.character would equal 0 
        for the Troll, 1 for the Elf, and so forth.  
        
        The variable self.character has been instantiated for your convenience below.
        
        Here is sample code for including an image on a page:   (char is a Character object)
            imageSmall = tkinter.PhotoImage(file="images/" + char.small_image);
            w= tkinter.Label (self,
                        image = imageSmall, 
                         )
            w.photo = imageSmall

            w.grid (ADD PARAMETERS HERE)
        '''
        self.character = tkinter.StringVar()
        self.character.set(None)
        row = 2
        char_pos = 0
        
        
        tkinter.Label(self, text = "Please choose a character:", font = "Times 12").grid(row = 1, column = 0, sticky = tkinter.W)
        
        hp = tkinter.Label(self, text = "            Hp: ", font = "Times 11 bold")
        hp.grid(row = 1, column = 2, sticky = tkinter.W)
        Tooltip(hp, "This is the amount of damage you can take")
        
        streng = tkinter.Label(self, text = "            Str: ", font = "Times 11 bold")
        streng.grid(row = 1, column = 3, sticky = tkinter.W)
        Tooltip(streng, "This is the amount of damage, divided by 2, you can give to the opponent")
        
        if self.choice == "battle1":
            defe = tkinter.Label(self, text =  "            Def: ", font = "Times 11 bold")
            defe.grid(row = 1, column = 4, sticky = tkinter.W)
            Tooltip(defe, "This is the amount of defense, divided by 4, that you can block the enemy's damamge by")
        else:
            dex = tkinter.Label(self, text = "            Dex: ", font = "Times 11 bold")
            dex.grid(row = 1, column = 4, sticky = tkinter.W)
            Tooltip(dex, "This is the amount that determines if you land your attack or not")
        
        for character in self.char_list.character_list:
            image = tkinter.PhotoImage(file = "images/" + character.small_image)
            
            tkinter.Radiobutton(self, text = character.name, variable = self.character,
                                 value = char_pos, font = "Arial 11").grid(row = row, column = 0, sticky = tkinter.W, columnspan = 2)
            
            photos = tkinter.Label(self, image = image)
            
            photos.photo = image
            
            photos.grid(row = row, column = 1, sticky = tkinter.W)
            
            if self.choice == "battle1":
                tkinter.Label(self, text = "\t" + str(character.hit_points), font = "Arial 11").grid (column = 2, row = row, sticky = tkinter.W)
                tkinter.Label(self, text = "\t" + str(character.strength), font = "Arial 11").grid(column = 3, row = row)    
                tkinter.Label(self, text = "\t" + str(character.defense), font = "Arial 11").grid(column = 4, row = row)
            else:
                tkinter.Label(self, text = "\t" + str(character.hp), font = "Arial 11").grid(column = 2, row = row)
                tkinter.Label(self, text = "\t" + str(character.strength1), font = "Arial 11").grid(column = 3, row = row)    
                tkinter.Label(self, text = "\t" + str(character.dexterity), font = "Arial 11").grid(column = 4, row = row)
            
            row += 1
            char_pos += 1
        
        tkinter.Button(self, text = "Next", command = self.continue_clicked, font = "helvetica 20", bg = "Lime").grid(row = row, column = 10)
        
    def continue_clicked(self):
        ''' This method is called when the Next button is clicked. 
            Notice that it passes self.character back to the callback method. '''
        self.call_on_selected(self.character.get())