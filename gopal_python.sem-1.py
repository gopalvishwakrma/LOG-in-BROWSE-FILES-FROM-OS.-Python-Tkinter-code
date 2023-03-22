#importing tkinter module
import os
import tkinter
import tkinter.ttk
from tkinter import*
import tkinter.messagebox
from tkinter import filedialog

def login():
    username = "gopal"
    password = "123456"
    if username_entry.get() == username and userpassword_entry.get() == password:
        tkinter.messagebox.showinfo(title = "Login success", message = "YOU SUCCESSFULLY LOGED IN.\n                 😁👍")
        window_2 = Tk()
        window_2.title = ("SAVING CONTENT")
        window_2.geometry("500x500")
        window_2.configure(bg = "#FFCBA4")

        #creating labels
        labels_window_2 = tkinter.Label(window_2, text = "*.*.*. FILE EXPLORING .*.*.*", width = 20 , bg = "#FFCBA4", fg = "black",
                                        font = ("Perpetua Titling MT", 30, "bold"))
        labels_window_2.place(x=460, y=53)

        #creating a function for browsing file
        def browse_file():
            filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                  filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
            if filename:
                os.startfile(filename)

        button_explore = tkinter.Button(window_2, text ="Browse Files", command = browse_file, width = 10,
                                        bg ='#DCD0FF', fg ='blue', font = ("bold", 20))
        button_explore.place(x = 500, y = 400)

        button_exit = Button(window_2, text = "Exit", command = window_2.destroy, width = 10, bg = '#DCD0FF', fg = 'red', font = ("bold", 20))
        button_exit.place(x = 850, y = 400)

        window.withdraw()
        window_2.mainloop()
    else:
        tkinter.messagebox.showerror(title="Error", message="INVALID INPUT.\n      🤔🤔")

#creating main window
window = Tk()
window.title("LOGIN PAGE")
window.geometry("340x440")
window.configure(bg = "#FFCBA4")

#creating labels
login_label = tkinter.Label(window, text = " *.*.*. LOGIN PAGE .*.*.*", width = 20 , bg = "#FFCBA4", fg = "black", font = ("Algerian", 30, "bold"))
login_label.place(x = 500, y = 53)

#Create the input label and entry box for username
username_label = tkinter.Label(window, text = "ENTER USERNAME*", bg = "#FFCBA4",
                               fg = "black", width = 40, font = ("bold", 20))
username_label.place(x = 300, y = 250)
username_entry = Entry(window, show = "*")
username_entry.place(x = 790, y = 258)

#Create the input label and entry box for password
userpassword_label = tkinter.Label(window, text = "PASSWORD*", bg = "#FFCBA4",
                                   fg = "black", width = 40, font = ("bold", 20))
userpassword_label.place(x = 300, y = 345)
userpassword_entry = Entry(window, show = "*")
userpassword_entry.place(x = 790, y = 350)

label_title = tkinter.Label(window, text = "THIS PROJECT IS MADE BY GOPAL VISHWAKARMA\nFROM MVLU COLLEGE ANDHERI EAST MUMBAI\nCONTACT: 8928578161 "
                                           "EMAIL: vishwakarmagopalcs222343@gmail.com", bg = "#FFCBA4", fg = "black", width = 60, font = ("arial",10))
label_title.place(x = 530, y = 770)

#Create the submit button
userbutton = tkinter.Button(window, text = "  LOGIN  ", command = login, width=10,
                            bg='#DCD0FF', fg='blue', font = ("bold", 20))

userbutton.place(x = 690, y = 600)
#Create the result label

result_label = tkinter.Label(window, text="")
result_label.pack()

#Run the application
window.mainloop()
window_2.mainloop()
