import tkinter

class Main_menu(tkinter.Frame):
    def __init__(self, master, callback):
        super(Main_menu, self).__init__(master)
        self.callback = callback
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        logo = tkinter.PhotoImage(file = "images/background.gif")
        background_label = tkinter.Label(self, image = logo)
        background_label.image = logo
        background_label.grid(column = 0, row = 0, sticky = tkinter.W, columnspan = 3, rowspan = 50)
        
        tkinter.Button(self, text = "Brain Battle", command = self.select_battle1, bg = "DodgerBlue", font = "Impact 18").grid(row = 39, column = 1)
        tkinter.Button(self, text = "Classic Battle", command = self.select_battle2, bg = "SpringGreen", font = "Impact 18").grid(row = 38, column = 1)
        tkinter.Button(self, text = "Exit", command = self.quit, bg = "Red", font = "Impact 16").grid(row = 40, column = 1)
    
    def select_battle1 (self):
        self.callback("battle1")
        
    def select_battle2 (self):
        self.callback("battle2")