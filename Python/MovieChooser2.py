import tkinter

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        tkinter.Label(self, text = "Choose your favorite type of movie").grid(row = 0, column = 0, sticky = tkinter.W)
        tkinter.Label(self, text = "Select one:").grid(row = 1, column = 0, sticky = tkinter.W)
        
        self.favorite = tkinter.StringVar()
        self.favorite.set(None)
        """create variable for single favorite type of movie. Only one radio button in a group can be selected
        at one time, there's no need for each radio buttons  to have its own status variable, instead a
        group of radio buttons share one special object that reflects which radio button is selected. The 
        StringVar class allows a string to be stored and retrieved. Created a single stringvar object for all
        the radio buttons to share, assign it to the attribute favorite, and set its initial value to None 
        using the objects set method"""
        
        tkinter.Radiobutton(self, text = "Comedy", variable = self.favorite,
                             value = "comedy", command = self.update_txt).grid(row = 2, column = 0, sticky = tkinter.W)
        tkinter.Radiobutton(self, text = "Drama", variable = self.favorite,
                             value = "drama", command = self.update_txt).grid(row = 3, column = 0, sticky = tkinter.W)
        tkinter.Radiobutton(self, text = "Romance", variable = self.favorite,
                             value = "romance", command = self.update_txt).grid(row = 4, column = 0, sticky = tkinter.W)
        #When whichever button is selected, the stringvar referenced by self.favorite should store the genre
        #The value becomes the value of the variable
        
        self.result_txt = tkinter.Text(self, width = 40, height = 5, wrap = tkinter.WORD)
        self.result_txt.grid(row = 5, column = 0, columnspan = 3)
        
    def update_txt(self):
        message = "Your favorite type of movie is "
        message += self.favorite.get()
        #gets the genre that you picked as your favorite
        
        self.result_txt.delete(0.0, tkinter.END)
        self.result_txt.insert(0.0, message)
        
root = tkinter.Tk()
root.title("Movie Chooser 2")

frame = Application(root)

root.mainloop()