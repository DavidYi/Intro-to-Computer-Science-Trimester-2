import tkinter

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        self.instruction_label = tkinter.Label(self, text = "Enter password for the secret of longevity")
        self.instruction_label.grid(row=0, column = 0, columnspan = 2,  sticky = tkinter.W)
        #Used Grid layout manager
        #Row and column parameters take integers and define where an object is placed within its master widget.
        #Can imagine the frame in the root window as a grid, divided into rows and columns.
        #columnspan lets you span a widget over more than one column, 
        #so in this case it allows long label to span 2 columns and it is the same concept with rowspan
        #sticky lets you move the widget in a direction in a cell, which is the row and column intersection
        #W is for west
        self.password_label = tkinter.Label(self, text = "Password: ")
        self.password_label.grid(row = 1, column = 0 , sticky = tkinter.W)
        #create label for password
        
        self.password_entry = tkinter.Entry(self)
        #entry lets the user enter something
        self.password_entry.grid(row = 1, column = 1, sticky = tkinter.W)
        #Creates a place to enter the password
        
        self.submit_button = tkinter.Button(self, text = "Submit", command = self.reveal)
        #binded the activation of the button with the reveal method, which reveals the secret 
        #if the user as entered the correct password
        self.submit_button.grid(row = 2, column = 0, sticky = tkinter.W)
        
        self.secret_txt = tkinter.Text(self, width = 35, height = 5, wrap = tkinter.WORD)
        #width and height sets the dimensions of the text box
        #wrap determines how the text in the box is wrapped. Can have WORD, CHAR, and NONE
        #the word  wraps entire words when you reach the right edge of the text box.
        #none means no wrapping and char wraps characters, when you get to right edge, the next char appears in
        #next line
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = tkinter.W)
        
    def reveal(self):
        contents = self.password_entry.get()
        
        if contents == "secret":
            message = "Here's the secret to living to 100: live to 99 and then be VERY careful."
        
        else:
            message = "That's not the correct password, so I can't share the secret with you"
        
        self.secret_txt.delete(0.0, tkinter.END)
        #this delete text from text-based widgets.
        #Pass 0.0 as the starting point meaning that the method should delete text starting at row 0, column 0
        #of the textbox. END is the endpoint, meaning to the end of the text. This deletes the text from
        #begginning to the end.
        self.secret_txt.insert(0.0, message)
        #method cna insert a string into a text based widget. method takes insert position and string
        #insert starts at row 0, column 0 and pass message, so that the value of it shows up in textbox
          
root = tkinter.Tk()
root.title("Longevity")
root.geometry("300x150")

frame = Application(root)

root.mainloop()