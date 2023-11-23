from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password = code.get()
    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="white")
        message = text_1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")
        Label(screen2, text="DECRYPT", font="courier", fg="green", bg="white").place(x=10, y=0)
        text_2 = Text(screen2, font="courier 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text_2.place(x=10, y=40, width=380, height=150)
        text_2.insert(END, decrypt)
    elif password == "":
        messagebox.showerror("Decryption", "Please Fill the Password!\nTry Again :/")
    elif password != "1234":
        messagebox.showerror("Decryption", "Password is Invalid!\nTry Again :/")

def encrypt():
    password = code.get()
    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="white")
        message = text_1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")
        Label(screen1, text="ENCRYPT", font="courier", fg="red", bg="white").place(x=10, y=0)
        text_2 = Text(screen1, font="courier 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text_2.place(x=10, y=40, width=380, height=150)
        text_2.insert(END, encrypt)
    elif password == "":
        messagebox.showerror("Encryption", "Please Fill the Password!\nTry Again :/")
    elif password != "1234":
        messagebox.showerror("Encryption", "Password is Invalid!\nTry Again :/")



def main_screen():
    global screen, text_1, code
    screen = Tk()
    screen.geometry("377x398")
    screen.resizable(False, False)
    img = PhotoImage(file="img/MugBit.PNG")
    screen.iconphoto(False, img)
    screen.title("Encryption and Decryption Program!")
    ############################### Functions #######################################
    def reset():
        code.set("")
        text_1.delete(1.0, END)
    ###############################   Code   #######################################
    Label(text="Enter the Text for\nEncryption and Decryption", fg="green", font=("Courier", 17)).place(x=10, y=10)
    text_1 = Text(font="Courier 12", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text_1.place(x=10, y=70, width=355, height=100)
    Label(text="Enter Secret Key for\nEncryption and Decryption!", fg="green", font=("Courier", 17)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, width=18, bd=0, font=("Courier", 25), show="#").place(x=10, y=230)
    Button(text="ENCRYPT", height="2", width="23", bg="#B31312", fg="white", bd=0, command=encrypt).place(x=10, y=280)
    Button(text="DECRYPT", height="2", width="23", bg="#9ADE7B", fg="white", bd=0, command=decrypt).place(x=200, y=280)
    Button(text="RESET", height="2", width="50", bg="#0766AD", fg="white", bd=0,command=reset).place(x=10, y=320)
    screen.mainloop()

main_screen()