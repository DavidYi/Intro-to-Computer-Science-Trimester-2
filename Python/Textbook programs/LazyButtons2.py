import tkinter

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        #This initializes the frame
        #we pass application object's master, so it gets properly set as the master.
    def create_widgets(self):
        self.button1 = tkinter.Button(self, text = "I do nothing")
        self.button1.grid()
        
        self.button2 = tkinter.Button(self)
        self.button2.grid()
        self.button2.configure(text = "Me too!")
        
        self.button3 = tkinter.Button(self)
        self.button3.grid()
        self.button3["text"] = "Same here!"
        #made 3 buttons
        """this is similar to the original lazy buttons. The difference is that the buttons are attributes of
        an Application object. Another difference is that he used self instead of the master for the buttons
        so that the Application object is their master"""
        
root = tkinter.Tk()
root.title("Lazy Buttons 2")
root.geometry("200x85")
#Same as the original

frame = Application(root)
#Instantiate an Application object with the root window as its master. The Application object's constructor
#invokes the create_widgets() method. HTis methond then creates buttons with the object as the master

root.mainloop()