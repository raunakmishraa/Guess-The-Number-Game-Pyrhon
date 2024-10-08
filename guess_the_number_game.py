#Import Modules
from tkinter import *
import random
import webbrowser
import os
#Functions
#Open my Website in Browser
def openWebsite(url):
    webbrowser.open_new(url)
#Game Algorithm
count=0
number=random.randint(1,100) #Selects a random integer between 0 to 100
def guessNumber():
    global count
    count=count+1
    attemptNo.configure(text=str(count))
    if count<11:
        guess=int(guess_entry.get())
        if guess<number:
            hint2.configure(text="The number you guessed is less than mine.")
        if guess>number:
            hint2.configure(text="The number you guessed is greater than mine.")
        if guess==number:
            attempts=str(count)
            hint2.configure(text="")
            result.configure(text=f"Whoa!! You guessed my number in {attempts} guesses!")
            warning.configure(text="Please restart to play again !!")
    if count==11:
        answer=str(number)
        result.configure(text=f"Nope... The number I was thinking of was {number}.")
    if count>11:
        warning.configure(text="Please restart to play again!!")
#Restart
def restart():
    root.destroy()
    os.startfile("guess_the_number_game.py")
#GUI
root=Tk()
root.title("Guess The Number Game") #Gives a title to the Window
root.geometry("750x580") #Sets the Geometry Size of Window
root.iconbitmap('Brand-Logo-Icon.ico') #Icon for the Window
root.resizable(False, False) #Restricts user to resize the Window
root.configure(bg='lemon chiffon') #Background Color dor Window
appLabel = Label(root, text="Guess The Number", font=("Times", "42", "bold italic"), fg="red", bg='lemon chiffon', anchor=CENTER) #Label for Appname
appLabel.pack() #Packs appLabel
appLabel.place(x=10,y=5) #Position for appLabel
attemptLabel = Label(root, text="Attempts: ", font=("Times", "20"), fg="green", bg='lemon chiffon', anchor=CENTER) #Label for attemptLabel
attemptLabel.pack() #Packs attemptLabel
attemptLabel.place(x=75,y=75) #Position for attemptLabel
attemptNo = Label(root, text="0", font=("Times", "20"), fg="black", bg='lemon chiffon', anchor=CENTER) #Label for attemptNo
attemptNo.pack() #Packs attemptNo
attemptNo.place(x=190,y=75) #Position for attemptNo
guess_frame = LabelFrame(root, text="Your Guess", background="lemon chiffon", bd=4, fg='red', labelanchor=N) #Creates a frame for Guess Boxes
guess_label = Label(guess_frame, text="Guess: ", font=("Helvetica", "15"), background="lemon chiffon") #Creates guess_label
guess_label.grid(row=0, column=2, padx=10, pady=10) #Position for guess_label
guess_entry = Entry(guess_frame, font=("Helvetica", "15")) #Creates guess_entry
guess_entry.grid(row=0, column=3, padx=10, pady=10) #Position for guess_entry
guess_button = Button(guess_frame, text="Check Guess", fg='white', bg='red', font=("Helvetica", "13", "italic"), bd='3', command=guessNumber) #Creates guess_button
guess_button.grid(row=1, column=3, padx=10, pady=5) #Position guess_button
guess_frame.pack() #Packs Guess Frame
guess_frame.place(x=215, y=125) #Positions guess_frame
hintLabel = Label(root, text="Hint:", font=("Times", "25", "underline"), fg="red", bg="lemon chiffon")
hintLabel.pack()
hintLabel.place(x=350, y=250)
hint = Label(root, text="I am thinking of a number between 1 and 100!!!", font=("Times", "18"), fg="blue", bg="lemon chiffon")
hint.pack()
hint.place(x=175, y=290)
hint2 = Label(root, text="", font=("Times", "18"), fg="blue", bg="lemon chiffon")
hint2.pack()
hint2.place(x=185, y=325)
resultLabel = Label(root, text="Result:", font=("Times", "25", "underline"), fg="red", bg="lemon chiffon")
resultLabel.pack()
resultLabel.place(x=338, y=360)
result = Label(root, text="", font=("Times", "18"), fg="black", bg="lemon chiffon")
result.pack()
result.place(x=175, y=400)
warning=Label(root, text="", font=("Times", "18"), fg="orange", bg="lemon chiffon")
warning.pack()
warning.place(x=250, y=425)
restart_button = Button(root, text="Restart", fg='white', bg='green', font=("Helvetica", "13", "italic"), bd='3', command=restart) #Creates restart_button
restart_button.pack()
restart_button.place(x=375, y=460)
#DEVELOPER LABEL
devNameLabel = Label(root, text="Developed By:", font=("Times", "20", "underline"), fg="green", bg="lemon chiffon")
devNameLabel.pack()
devNameLabel.place(x=225, y=500)
devName = Label(root, text="Raunak Kumar", font=("Times", "20"), fg="orange", bg="lemon chiffon")
devName.pack()
devName.place(x=400, y=500)
devContact = Label(root, text="Lets Connect", fg="blue", cursor="hand2")
devContact.pack()
devContact.place(x=350, y=540)
devContact.bind("<Button-1>", lambda e: openWebsite("https://www.raunakmishra.com.np/#Contact"))
root.mainloop()
