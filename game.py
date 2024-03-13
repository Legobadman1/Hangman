from tkinter import *
import hangmanwords


word = hangmanwords.randomlocation()
blank = []
lives = 8
wrong = set()

for _ in range(len(word)):
    blank.append("_")
blankword = " ".join(blank)


def initialize_game_animals():
    global word, blank, lives
    word = hangmanwords.randomanimal()
    initialise_game()


def initialize_game_location():
    global word
    word = hangmanwords.randomlocation()
    initialise_game()


def initialise_game():
    global word, blank, lives
    blank = ["_" for _ in word]
    lives = 8
    label1.config(text=" ".join(blank))
    canvas1.delete("all")
    answer.config(state=NORMAL)
    submit.config(state=NORMAL)
    frame3.place_forget()
    frame4.place_forget()
    wrong.clear()
    label5.config(text="")
    frame5.destroy()


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
        wrong.add(guess)
        label5.config(text=", ".join(list(wrong)))
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
root.geometry("600x675")
root.config(bg="light blue")
root.title("Hangman")
root.iconphoto(True, smile)

blankword = ""
label1 = Label(root, text=blankword, font=("Courier New", 30, "bold"), bg="light blue")
label1.pack()

frame1 = Frame(root)
frame1.pack()
canvas1 = Canvas(frame1, width=500, height=450)
canvas1.pack()

frame3 = Frame(root)
label2 = Label(
    frame3, text="You lost! 😞", font=("Courier New", 25, "bold"), bg="#d65864"
)
label2.pack()
play1 = Button(
    frame3,
    text="Play animals",
    command=initialize_game_animals,
    font=("Courier New", 25, "bold"),
    bg="#5c5c5c",
    fg="#3ad406",
    activebackground="#000000",
    activeforeground="#3ad406",
    bd=5,
)
play1.pack()
play2 = Button(
    frame3,
    text="Play locations",
    command=initialize_game_location,
    font=("Courier New", 25, "bold"),
    bg="#5c5c5c",
    fg="#3ad406",
    activebackground="#000000",
    activeforeground="#3ad406",
    bd=5,
)
play2.pack()

frame4 = Frame(root)
label3 = Label(
    frame4, text="You won! 🤩", font=("Courier New", 25, "bold"), bg="#6fde7e"
)
label3.pack()
play3 = Button(
    frame4,
    text="Play animals",
    command=initialize_game_animals,
    font=("Courier New", 25, "bold"),
    bg="#5c5c5c",
    fg="#3ad406",
    activebackground="#000000",
    activeforeground="#3ad406",
    bd=5,
)
play3.pack()
play4 = Button(
    frame4,
    text="Play locations",
    command=initialize_game_location,
    font=("Courier New", 25, "bold"),
    bg="#5c5c5c",
    fg="#3ad406",
    activebackground="#000000",
    activeforeground="#3ad406",
    bd=5,
)
play4.pack()

frame2 = Frame(root, bg="light blue", width=500)
frame2.pack()

answer = Entry(frame2, width=15, font=("Courier New", 25), state=DISABLED)
answer.pack(side="left")
answer.bind("<Return>", submitting)

label6 = Label(frame2, text="", bg="light blue")
label6.pack(side="left")

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
    state=DISABLED,
)
submit.pack(side="right")

exitB = Button(
    root,
    text="Quit",
    font=("Courier New", 18, "bold"),
    padx=10,
    pady=5,
    bg="#c70404",
    activebackground="#99000f",
    relief=RAISED,
    command=quit,
)
exitB.place(relx=1, rely=1, anchor="se")

label4 = Label(
    root, text="Wrong letters:", font=("Courier New", 18, "bold"), bg="light blue"
)
label4.pack()

label5 = Label(root, text="", font=("Courier New", 18, "bold"), bg="light blue")
label5.pack()

frame5 = Frame(root)
frame5.place(relx=0.5, rely=0.5, anchor=CENTER)
animal = Button(
    frame5,
    text="Animals",
    command=initialize_game_animals,
    font=("Courier New", 18, "bold"),
    bg="#606175",
    activebackground="#3f3f4d",
    fg="red",
    activeforeground="red",
    bd=5,
    relief=RAISED
)
animal.pack()
location = Button(
    frame5,
    text="General locations",
    command=initialize_game_location,
    font=("Courier New", 18, "bold"),
    bg="#606175",
    activebackground="#3f3f4d",
    fg="light green",
    activeforeground="light green",
    bd=5,
    relief=RAISED
)
location.pack()

root.mainloop()
