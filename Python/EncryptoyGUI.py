from encryptor import Encryptor
import tkinter
import random

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.file_name = ["cipher1.txt", "cipher2.txt"]
        self.create_widgets()
    
    def create_widgets(self):
        self.hide_children2()
        
        tkinter.Label(self, text = "Choose a file to start.").grid(row = 0, column  = 0, columnspan = 3)
        
        row = 1
        
        self.file = tkinter.StringVar()
        self.file.set(None)
                
        for file in self.file_name:
            row +=1
            tkinter.Radiobutton(self, text = file, variable = self.file, value = file).grid(row = row, column = 2)
        
        
        row += 1
        
        tkinter.Button(self, text = "Continue", command = self.hide_children, bg = "Lime").grid(row = row, column = 3)
        tkinter.Button(self, text = "Quit", command = self.quit, bg = "red").grid(row = row, column = 4, columnspan = 2)
        
    def hide_children(self):
        #when you want to go edit the story
        #gets rid of the widgets in the frame
        if (self.file.get() != self.file_name[0]) and (self.file.get() != self.file_name[1]) :
            tkinter.Label(self, text = "Please choose a file", bg = "Yellow", fg = "Crimson").grid(row = 1, column = 2, columnspan = 2)
            
        else:
            for widget in self.winfo_children():
                widget.destroy()
            self.create_second_widgets()
    
    def create_second_widgets(self):
        tkinter.Label(self, text = "Choose what you would like to do.").grid(row = 0, column = 2, columnspan = 3)
        
        self.enc = Encryptor(self.file.get())
        
        #tkinter.Button(self, text = "Create Cipher Key", command = self.create_key).grid(row = 1, column = 2, columnspan = 3)
        tkinter.Button(self, text = "Encrypt/Decrypt", command = self.tools, bg = "Lime").grid(row = 2, column = 2)
        tkinter.Button(self, text = "Choose New File", command = self.create_widgets, bg = "RoyalBlue").grid(row = 4, column = 2)
        tkinter.Button(self, text = "Quit", command = self.quit, bg = "Red").grid(row = 5, column = 2)
    
    def hide_children2(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    def tools(self):
        self.hide_children2()
        
        tkinter.Button(self, text = "Back", command = self.hide_children, bg = "RoyalBlue").grid(row = 0, column = 0, columnspan  = 4, sticky = tkinter.W)
        tkinter.Label(self, text = "Please input a message, whether encrypted or not.").grid(row = 0, column = 1, columnspan = 20, sticky = tkinter.W)
        
        self.msg_entry = tkinter.Text(self, height = 10, width = 75, wrap = tkinter.WORD)
        self.msg_entry.grid(row = 1, column = 0, columnspan = 10)
        tkinter.Button(self, text = "Encrypt", command = self.encrypt, bg = "Lime").grid(row = 2, column = 4)
        tkinter.Button(self, text = "Quit", command = self.quit, bg = "Red").grid(row = 2, column = 5)
        tkinter.Button(self, text = "Decrypt", command = self.decrypt, bg = "Lime").grid(row = 2, column = 6)
        
        tkinter.Label(self, text = "Decrypted/Encrypted Message:").grid(row = 3, column = 0, columnspan = 5, sticky = tkinter.W)
        self.msg_text = tkinter.Text(self, height = 10, width = 75, wrap = tkinter.WORD)
        self.msg_text.grid(row = 4, column = 0, columnspan = 20)
 
    def textbox(self):
        self.msg_text.delete(0.0, tkinter.END)
        self.msg_text.insert(0.0, self.msg)
        
    def encrypt(self):
        self.msg = self.enc.encrypt_message(self.msg_entry.get(0.0, tkinter.END))
        #Need this because the textbox is multi line, so you need points20
        self.textbox()
        
    def decrypt(self):
        self.msg = self.enc.decrypt_message(self.msg_entry.get(0.0, tkinter.END))
        self.textbox()

root = tkinter.Tk()
root.title("Encryptor/Decryptor")
frame = Application(root)
root.mainloop()