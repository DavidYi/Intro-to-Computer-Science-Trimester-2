import tkinter
from Tooltip import Tooltip

class Screen_Battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, call_on_next):
        super(Screen_Battle, self).__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hp
        self.player2_max_hp = player2.hp

        # Save the method reference to which we return control after this page Exits.
        self.call_on_selected = call_on_next
        
        self.choice = "battle2"
        
        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        '''
        This method creates all of the widgets for the battle page.
        '''
        self.is_alive = True
        
        column = 1
        playerlist = [self.player1, self.player2]
        
        tkinter.Button(self, text = "Exit", command = self.exit_clicked, bg = "Red",  font = "Helvetica 13").grid(row = 0, column = 0, sticky = tkinter.W)
        
        for player in playerlist:
            image = tkinter.PhotoImage(file = "images/" + player.large_image)
            photos = tkinter.Label(self, image = image)
            photos.photo = image   
            photos.grid(row = 3, column = column)
            
            tkinter.Label(self, text = "Name: " + player.name, font = "Arial 13").grid(column = column, row = 4)
            if column == 1:
                self.label1 =tkinter.Label(self, text = "Hp: " + str(player.hp)+ "/" + str(self.player1_max_hp), font = "Arial 12")
                self.label1.grid(column = column, row = 5)
            else:
                self.label2 = tkinter.Label(self, text = "Hp: " + str(player.hp)+ "/" + str(self.player2_max_hp), font = "Arial 12")
                self.label2.grid(column = column, row = 5)
            
            column += 2
        
        self.lastbutt = tkinter.Button(self, text = "Attack", command = self.attack_clicked, bg = "Black", fg = "Red", font = "Impact 14")
        self.lastbutt.grid(column = 2, row = 4)
        Tooltip(self.lastbutt, "This attacks your opponent")
        
        self.textbox = tkinter.Text(self, width = 55, height = 10, wrap = tkinter.WORD)
        self.textbox.grid(row = 6, column = 0, columnspan = 50)
        
        
    def attack_clicked(self):
        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and the computer.
            2) Updates the labels on the top right with the result of the attacks.
            3) Determines if there is a victor.
            4) If there is a victor, removes that Attack button and replaces it with an Exit button.     
        '''        
        msg1 = self.player1.attack(self.player2, False, False, self.choice)
        msg2 = self.player2.attack(self.player1, False, False, self.choice)
        deadmsg = ""
        
        self.textbox.insert(tkinter.END, msg1)
        self.textbox.insert(tkinter.END, "\n" + msg2 + "\n\n")
        
        if self.player1.hp <= 0:
            deadmsg += str(self.player1.die())
            self.is_alive = False
            self.label1["text"] = "Hp: " + str(0)+ "/" + str(self.player1_max_hp)
        
        if self.player2.hp <=0:
            deadmsg += "\n" + str(self.player2.die())
            self.is_alive = False
            self.label2["text"] = "Hp: " + str(0)+ "/" + str(self.player2_max_hp)
            
        if self.is_alive == False:
            self.textbox.insert(tkinter.END,deadmsg + "\n")
            self.lastbutt.destroy()
        
        self.textbox.see(tkinter.END)
        
        if self.player1.hp > 0:
            self.label1["text"] = "Hp: " + str(self.player1.hp)+ "/" + str(self.player1_max_hp)
        elif self.player2.hp > 0:
            self.label2["text"] = "Hp: " + str(self.player2.hp)+ "/" + str(self.player2_max_hp)
        
                                     
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.call_on_selected()          
            