import tkinter

class Screen_prepare_to_battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, call_on_next, choice):
        super(Screen_prepare_to_battle, self).__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.call_on_selected = call_on_next
        
        self.choice = choice
        
        self.create_widgets()
        self.grid()
        
    
    def create_widgets (self):
        '''
        This method creates all of the widgets the prepare to battle page.
        '''
        column = 1
        playerlist = [self.player1, self.player2]
        
        tkinter.Label(self, text = "Time to battle!").grid(column = 2, row = 0)
        '''
        x = "dwarf_300.gif"
        background_image=tkinter.PhotoImage(file = "images/" + x)
        background_label = tkinter.Label(self, image = background_image)
        background_label.photo = background_image
        background_label.pack(side = "bottom", fill = "both", expand = "yes")#place(x=0, y=0, relwidth=1, relheight=1)
        '''
        
        for player in playerlist:
            image = tkinter.PhotoImage(file = "images/" + player.large_image)
            photos = tkinter.Label(self, image = image)
            photos.photo = image   
            photos.grid(row = 3, column = column)
            
            if self.choice == "battle1":
                tkinter.Label(self, text = "Name: " + player.name, font = "Arial 11").grid(column = column, row = 4)
                tkinter.Label(self, text = "Hp: " + str(player.hit_points), font = "Arial 11").grid(column = column, row = 5)
                tkinter.Label(self, text = "Str: " + str(player.strength), font = "Arial 11").grid(column = column, row = 6)    
                tkinter.Label(self, text = "Def: " + str(player.defense), font = "Arial 11").grid(column = column, row = 7)
            else:
                tkinter.Label(self, text = "Name: " + player.name, font = "Arial 11").grid(column = column, row = 4)
                tkinter.Label(self, text = "Hp: " + str(player.hp), font = "Arial 11").grid(column = column, row = 5)
                tkinter.Label(self, text = "Str: " + str(player.strength1), font = "Arial 11").grid(column = column, row = 6)    
                tkinter.Label(self, text = "Dex:" + str(player.dexterity), font = "Arial 11").grid(column = column, row = 7)
                
            column += 2
        
        tkinter.Label(self, text = "VS.", font = "Times 40").grid(row = 4, column = 2, rowspan = 12)
        
        tkinter.Button(self, text = "Let's Battle", command = self.continue_clicked, bg = "Lime", font = "Helvetica 12").grid(row = 8, column = 3)
        
        
    def continue_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.call_on_selected()
            
        