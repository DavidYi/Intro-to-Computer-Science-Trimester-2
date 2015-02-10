import tkinter
from test.test_pathlib import only_nt
from tkinter.tix import COLUMN

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        tkinter.Label(self, text = "Choose your favorite movie types").grid(row = 0, column = 0, sticky = tkinter.W)
        #this label is not assigned to a variable because with tkinter, the label object is connected to the
        #program by its master like all GUI element. Meaning that if I know I don't need to directly access
        #a widget then I don't need to assign the object to a variable. Makes the code cleaner
        tkinter.Label(self, text = "Select all that apply: ").grid(row = 1, column = 0, sticky = tkinter.W)
        #Since this is not assigned to a variable, it is needed to use the grid after creating the label
        
        self.likes_comedy = tkinter.BooleanVar()
        """Every check button needs a special object associated with it that automatically reflects the check
        button status. Special object must be an instance of the BooleanVar class, which the variable can only
        be true or false"""
        
        tkinter.Checkbutton(self, text = "Comedy", variable = self.likes_comedy, command = self.update_txt
                            ).grid(row = 2, column = 0, sticky = tkinter.W)
        #This creates a new check button with the text, comedy and the variable being either true of false
        #By passing the self.update_txt() to the parameter comand, I bind the activation of the check button
        #with the method.
        
        self.likes_drama = tkinter.BooleanVar()
        tkinter.Checkbutton(self, text = "Drama", variable = self.likes_drama, command = self.update_txt
                            ).grid(row = 3, column = 0, sticky = tkinter.W)
        
        self.likes_romance = tkinter.BooleanVar()
        tkinter.Checkbutton(self, text = "Romance", variable = self.likes_romance, command = self.update_txt
                            ).grid(row = 4, column = 0, sticky = tkinter.W)
        
        self.results_txt = tkinter.Text(self, width = 40, height = 5, wrap = tkinter.WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)
        #Creates textbox
        
    def update_txt(self):
        likes = ""
        
        if self.likes_comedy.get():
            likes +="You like comedic movies.\n"
            
        if self.likes_drama.get():
            likes +="You like dramatic movies.\n"
            
        if self.likes_romance.get():
            likes +="You like romantic movies.\n"
        
        self.results_txt.delete(0.0, tkinter.END)
        self.results_txt.insert(0.0, likes)
        
root = tkinter.Tk()
root.title("Movie Chooser")

frame = Application(root)

root.mainloop()        