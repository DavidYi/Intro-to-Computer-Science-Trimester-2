import tkinter
from Tooltip import Tooltip
import random

class Screen_Battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, call_on_next):
        super(Screen_Battle, self).__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points
        
        # Save the method reference to which we return control after this page Exits.
        self.call_on_selected = call_on_next
        
        self.choice = "battle1"
        
        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        '''
        This method creates all of the widgets for the battle page.
        '''
        column = 0
        playerlist = [self.player1, self.player2]
        self.is_alive = True
        self.turn = 1
        self.attacklist = ["high", "low", "crit"]
        '''
        a = tkinter.Label(self)
        b = tkinter.Label(self)
        c = tkinter.Label(self)
        '''
        tkinter.Button(self, text = "Exit", bg = "red", command = self.exit_clicked, font = "Helvetica 13").grid(row = 0, column = 0, sticky = tkinter.W)
        
        for player in playerlist:
            image = tkinter.PhotoImage(file = "images/" + player.large_image)
            photos = tkinter.Label(self, image = image)
            photos.photo = image
            photos.grid(row = 3, column = column, columnspan = 3)
            
            tkinter.Label(self, text = "Name: " + player.name, font = "Arial 13").grid(column = column, row = 4)
            if column == 0:
                self.label1 = tkinter.Label(self, text = "Hp: " + str(self.player1.hit_points)+ "/" + str(self.player1_max_hp), font = "Arial 12")
                self.label1.grid(column = column, row = 5)
            else:
                self.label2 = tkinter.Label(self, text = "Hp: " + str(self.player2.hit_points)+ "/" + str(self.player2_max_hp), font = "Arial 12")
                self.label2.grid(column = column, row = 5)
            
            column += 3
        
        self.meth1 = tkinter.Button(self, text = "High Attack", command = self.high, bg = "DeepSkyBlue", font = "Impact 14")
        self.meth1.grid(column = 0,  row = 6)
        self.x = Tooltip(self.meth1, "Misses if the opponent ducks")
        
        self.meth2 = tkinter.Button(self, text = "Low Attack", command = self.low, bg = "ForestGreen", font = "Impact 14")
        self.meth2.grid(column = 1, row = 6, sticky = tkinter.W)
        self.y = Tooltip(self.meth2, "Misses if the opponent jumps")
        
        self.meth3 = tkinter.Button(self, text = "Critical Attack", command = self.crit, bg = "Gold", font = "Impact 14")
        self.meth3.grid(column = 0, row = 7, columnspan = 2)            
        self.z = Tooltip(self.meth3, "This attacks the opponent for 1.5 the damage, but if it misses or gets blocked, then you get the damage.")
        
        self.textbox = tkinter.Text(self, width = 55, height = 10, wrap = tkinter.WORD)
        self.textbox.grid(row = 6, column = 2, columnspan = 50, rowspan = 50)    
        
        self.computer_choice()
        
        self.enemy = self.player2
        self.player = self.player1
        
    def high(self):
        if self.turn%2 == 1:
            self.attackmeth = "high"
            self.defendmeth = self.computer
        else:
            self.defendmeth = "high"
            self.attackmeth = self.computer
        
        self.attack_clicked()
        
    def low(self):
        if self.turn%2==1:
            self.attackmeth = "low"
            self.defendmeth = self.computer
        else:
            self.defendmeth = "low"
            self.attackmeth = self.computer
        self.attack_clicked()
        
    def crit(self):
        if self.turn%2 == 1:
            self.attackmeth = "crit"
            self.defendmeth = self.computer
        else:
            self.defendmeth = "crit"
            self.attackmeth = self.computer
        self.attack_clicked()
        
    def attack_clicked(self):
        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and the computer.
            2) Updates the labels on the top right with the result of the attacks.
            3) Determines if there is a victor.
            4) If there is a victor, removes that Attack button and replaces it with an Exit button.     
        ''' 
        self.turn +=1
       
        if self.attackmeth == "crit":
            if self.attackmeth == self.defendmeth:
                msg = self.enemy.attack(self.player, True, True, self.choice)
            else:
                msg = self.player.attack(self.enemy, True, False, self.choice)
        else:
            if self.attackmeth == self.defendmeth:
                msg = self.enemy.name + " dodges " + self.player.name + "'s attack"
            else:
                msg = self.player.attack(self.enemy, False, False, self.choice)
        
        
        self.textbox.insert(tkinter.END, msg + "\n\n")
        
        if self.player1.hit_points <= 0:
            deadmsg = str(self.player1.die())
            self.is_alive = False
            
            self.label1["text"] = "Hp: " + str(0)+ "/" + str(self.player1_max_hp)
            
        if self.player2.hit_points <=0:
            deadmsg = str(self.player2.die())
            self.is_alive = False
            self.label2["text"] = "Hp: " + str(0)+ "/" + str(self.player2_max_hp)
    
            
        if self.is_alive == False:
            self.textbox.insert(tkinter.END,deadmsg + "\n")
            
            self.meth1.destroy()
            self.meth2.destroy()
            self.meth3.destroy()
            
        self.textbox.see(tkinter.END)
        
        self.x.close_window()
        self.y.close_window()
        self.z.close_window()
        
        self.hpcheck()
        
        if self.is_alive == True:
            self.computer_choice()
        
            if self.turn%2 == 1:
                self.meth1["text"] = "High Attack"
                self.x = Tooltip(self.meth1, "Misses if the opponent ducks")
                    
                self.meth2["text"] = "Low Attack"
                self.y = Tooltip(self.meth2, "Misses if the opponent jumps")
                    
                self.meth3["text"] = "Critical Attack"
                self.z = Tooltip(self.meth3, "This attacks the opponent for 1.5 times the damage, but if it misses or gets blocked, then you get the regular damage.")
                
                self.enemy = self.player2
                self.player = self.player1
                
            else:
                self.meth1["text"] = "Duck"
                self.x = Tooltip(self.meth1, "Nullifies high attacks")
                    
                self.meth2["text"] = "Jump"
                self.y = Tooltip(self.meth2, "Nullifies low attacks")
                    
                self.meth3["text"] = "Critical Defense"
                self.z = Tooltip(self.meth3, "Nullifies critical attacks and returns 1.5 times the expected damage")
                    
                self.enemy = self.player1
                self.player = self.player2
        else:
            self.meth1.destroy()
            self.meth2.destroy()
            self.meth3.destroy()
            
    def hpcheck(self):
        if self.is_alive == True:
            self.label1["text"] = "Hp: " + str(self.player1.hit_points)+ "/" + str(self.player1_max_hp)
            self.label2["text"] = "Hp: " + str(self.player2.hit_points)+ "/" + str(self.player2_max_hp)
    
    def computer_choice(self):
        pos = random.randrange(2)
        self.computer = self.attacklist[pos]
    
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.call_on_selected()