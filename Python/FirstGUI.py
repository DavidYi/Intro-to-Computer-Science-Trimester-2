import tkinter
#Has the graphics
#Always imports this for GUI
class Application (tkinter.Frame):
    #Creates application object and extends it from Frame
    def __init__(self, master):
        #Every window has a parent and a CHILD
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets (self):
        #Widgets are buttons and labels
        self.button_quit = tkinter.Button (self, text="Quit", bg="red")
        #Creates a button with it saying Quit and have a background(bg) to red
        self.button_quit.grid()
        #Adds the button to the screen
        self.button_quit["command"] = self.quit
        #Quit is prebuilt
        
        self.button_hi = tkinter.Button(self, text="Hi", bg="blue")
        self.button_hi["command"]=self.say_hi
        #We are not calling the function but just giving a reference of the command
        self.button_hi.grid()
    
    def say_hi(self):
        print("Hello! JOO FOOKIN PLEB!!!")
        
root = tkinter.Tk()
root.title("Say hi, joo pleb!")
root.geometry("200x85")
app = Application(root)

root.mainloop()