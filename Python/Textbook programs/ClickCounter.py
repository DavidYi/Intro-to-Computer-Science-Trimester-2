import tkinter

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application,self).__init__(master)
        self.grid()
        self.clicks = 0 #The number of button clicks
        self.create_widgets()
        #Initializes the frame
    
    def create_widgets(self):
        self.button = tkinter.Button(self)
        self.button["text"] = "Total Clicks: 0"
        self.button["command"] = self.update_count
        self.button.grid()
        #Set the button widget's command to the update_count() method. 
        #When the user clicks the button, the method is invoked.
        
    def update_count(self):
        self.clicks += 1
        self.button["text"] = "Total Clicks: " + str(self.clicks)
        #makes the button change its text in the box
    
root = tkinter.Tk()
root.title("Click Counter")
root.geometry("200x50")

frame = Application(root)

root.mainloop()