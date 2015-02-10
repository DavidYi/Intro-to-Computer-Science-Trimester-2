from encryptor import Encryptor

def main():
    file_dict = {"a": "cipher1.txt", "b": "cipher2.txt"}
        
    filename = choosefile(file_dict)
    enc = Encryptor(filename)
    choices(enc, file_dict)
    
def choices(enc, file_dict):
    x= False
    while x == False:
        print("F - Choose a Different File\nE - Encrypt Message\nD - Decrypt Message\nQ - Quit")
        choice = input()
            
        if choice.capitalize() == "F":
            choosefile(file_dict)
        elif choice.capitalize() == "E":
            encrypt(enc, file_dict)
            x = True
        elif choice.capitalize() == "D":
            decrypt(enc, file_dict)
            x = False
        elif choice.capitalize() == "Q":
            quit()
        else:
            print("Please choose a valid choice.")
    
def choosefile(file_dict):
    print("Please choose a file shown below to use as a cipher.")
    for key in list(file_dict.keys()):
        print(key + ") " + file_dict[key] + " ", end = "")
    file = input("\n").lower()
    
    return file_dict[file]
    
def encrypt(enc, file_dict):
    msg = input("Please enter the message you would like to encrypt.\n")
    encrypted = enc.encrypt_message(msg)
    print(encrypted)
    choices(enc, file_dict)
    
def decrypt(enc, file_dict):
    msg = input("Please enter the message you would like to decrypt.\n")
    decrypted = enc.decrypt_message(msg)
    print(decrypted)
    choices(enc, file_dict)

main()