from tkinter import *
from time import *
from random import randint

root = Tk()
root.title('Прямоугольник зеленый')
root.geometry('920x480')
root.configure(background='#fff')
holst = Canvas(root, bg='#fff', width=1920, height=1080, highlightbackground="#fff")
lab = Label(bg='#fff', font="20")
lab.pack()
counter = Label(bg='#fff', font="20")
counter.pack()


def koordX():
    x = randint(0, 1800)
    return x


def koordY():
    y = randint(0, 960)
    return y


def onClick():
    backTimer = 4
    btn.destroy()

    for x in range(4):
        backTimer -= 1
        if x == 3:
            backTimer = 'Start!'
        lab.config(text=str(backTimer))
        sleep(1)
        if backTimer == 'Start!':
            root.update()
            sleep(1)
            lab.destroy()
            target.place(x=koordX(), y=koordY())
        root.update()


count = 0


def onTargetClick():
    global count
    count += 1
    counter.config(text=str(count))

    target.place(x=koordX(), y=koordY())


btn = Button(
    text="Начало игры",
    background="#555",
    foreground="#ccc",
    padx="20",
    pady="8",
    font="20",
    width=20,
    command=onClick
)
btn.pack()
image = PhotoImage(file="pt.png")
target = Button(
    background="#fff",
    foreground="#fff",
    image=image,
    activebackground="#fff",
    highlightcolor="#fff",
    bd=0,
    command=onTargetClick
)
holst.pack()
holst.mainloop()
