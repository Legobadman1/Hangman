from tkinter import *
from hangman import randomword


word = randomword()
blank = []
lives = 8
for _ in range(len(word)):
    blank.append("_")
blankword = " ".join(blank)

def initialize_game():
    global word, blank, lives
    word = randomword()
    blank = ["_" for _ in word]
    lives = 8
    label1.config(text=" ".join(blank))
    canvas1.delete("all")
    answer.config(state=NORMAL)
    submit.config(state=NORMAL)
    frame3.place_forget()
    frame4.place_forget()

def submitting(key):
    global lives
    count = -1
    guess = answer.get().lower()
    answer.delete(0, END)
    if len(guess) != 1 or not guess.isalpha():
        return
    if guess in word:
        for i in word:
            count += 1
            if guess == i:
                blank[count] = i
                label1.config(text=" ".join(blank))
    else:
        lives -= 1
        if lives == 7:
            canvas1.create_rectangle(0, 80, 300, 90, fill="brown", width=5)
        elif lives == 6:
            canvas1.create_line(250, 90, 250, 175, width=5)
        elif lives == 5:
            canvas1.create_oval(200, 125, 300, 225, fill="light yellow", width=5)
        elif lives == 4:
            canvas1.create_line(250, 225, 250, 375, width=5)
        elif lives == 3:
            canvas1.create_line(250, 275, 200, 325, width=5)
        elif lives == 2:
            canvas1.create_line(250, 275, 300, 325, width=5)
        elif lives == 1:
            canvas1.create_line(250, 375, 200, 425, width=5)
        elif lives == 0:
            canvas1.create_line(250, 375, 300, 425, width=5)
            label1.config(text=word)
            answer.config(state=DISABLED)
            submit.config(state=DISABLED)
            frame3.place(relx=0.5, rely=0.5, anchor=CENTER)

    if "_" not in blank:
        label1.config(text=word)
        answer.config(state=DISABLED)
        submit.config(state=DISABLED)
        frame4.place(relx=0.5, rely=0.5, anchor=CENTER)


root = Tk()
smile = PhotoImage(file="smile.png")
root.geometry("600x700")
root.config(bg="light blue")
root.title("Hangman")
root.iconphoto(True, smile)


label1 = Label(root, text=blankword, font=("Courier New", 30, "bold"), bg="light blue")
label1.pack()

frame1 = Frame(root)
frame1.pack()
canvas1 = Canvas(frame1, width=500, height=500)
canvas1.pack()

frame3 = Frame(root)
label2 = Label(frame3, text="You lost! 😞", font=("Courier New", 25, "bold"), bg="#d65864")
label2.pack()
play1 = Button(frame3, text="Play again", command=initialize_game, font=("Courier New", 25, "bold"), bg="#5c5c5c", fg="#3ad406", activebackground="#000000", activeforeground="#3ad406", bd=5)
play1.pack()

frame4 = Frame(root)
label3 = Label(frame4, text="You won! 🤩", font=("Courier New", 25, "bold"), bg="#6fde7e")
label3.pack()
play2 = Button(frame4, text="Play again", command=initialize_game, font=("Courier New", 25, "bold"), bg="#5c5c5c", fg="#3ad406", activebackground="#000000", activeforeground="#3ad406", bd=5)
play2.pack()

answer = Entry(root, width=25, font=("Courier New", 25), state=NORMAL)
answer.pack()
root.bind("<Return>", submitting)

frame2 = Frame(root)
frame2.pack()
submit = Button(
    frame2,
    text="Enter",
    font=("Courier New", 18, "bold"),
    padx=10,
    pady=5,
    bg="#abb2c7",
    activebackground="#727782",
    relief=RAISED,
    command=submitting,
    state=NORMAL
)
submit.pack(side="left")
exitB = Button(
    frame2,
    text="Quit",
    font=("Courier New", 18, "bold"),
    padx=10,
    pady=5,
    bg="#abb2c7",
    activebackground="#727782",
    relief=RAISED,
    command=quit,
)
exitB.pack(side="left")

root.mainloop()
