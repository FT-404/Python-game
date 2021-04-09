from tkinter import *
from time import *
from random import randint
from PIL import Image, ImageTk

root = Tk()
image = PhotoImage(file="pt.png")
root.title('Прямоугольник зеленый')
root.geometry('1920x1080')
root.configure(background='#fff')
holst = Label(root, width=1920, height=1080, highlightbackground="#fff")
img = Image.open("bg2.jpg")
holst.img = ImageTk.PhotoImage(img)
holst['image'] = holst.img
lab = Label(bg='#6797ec', font="20")
count = 0
gameTimerLab = Label(bg='#6797ec', font='40')
counter = Label(bg='#6797ec', font="20")


def Starter():
    lab.place(x=950, y=20)
    counter.place_forget()
    global backTimer
    backTimer = 4
    gameTimer = 30
    btnRec.place_forget()
    btnMatch.place_forget()
    for x in range(4):
        backTimer -= 1
        if x == 3:
            backTimer = 'Start!'
        lab.config(text=str(backTimer))
        sleep(1)

        root.update()
    if backTimer == 'Start!':
        sleep(1)
        counter.place(x=950, y=70)
        gameTimerLab.place(x=930, y=20)
        timing = time()
        backTimer = ''
        lab.config(text=str(backTimer))
        target.place(x=koordX(), y=koordY())
        root.update()
        counter.config(text='Счёт: ' + str(count))
        while gameTimer != 0:
            if time() - timing > 1:
                timing = time()
                gameTimer -= 1
                print(gameTimer)
            gameTimerLab.config(text='Оставшееся время: ' + str(gameTimer))
            root.update()

        if gameTimer == 0:
            target.place_forget()

            if count % 10 == 1:
                ans = ' очко!'
            elif count % 10 >= 2 and count % 10 <= 4:
                ans = ' очка!'
            else:
                ans = ' очков!'
            counter.config(text='Вы набрали - ' + str(count) + ans)
            counter.place(x=920, y=70)
            gameTimer = ''
            gameTimerLab.config(text=gameTimer)
            btnRec.place(x=847.5, y=260)
            btnMatch.place(x=847.5, y=300)


def koordX():
    x = randint(0, 1800)
    return x


def koordY():
    y = randint(0, 960)
    return y


def onTargetClick():
    global count
    count += 1
    counter.config(text='Счёт: ' + str(count))
    target.place(x=koordX(), y=koordY())


def RecruitMod():
    Starter()


def MatchMod():
    global count
    count = 0
    Starter()


btnRec = Button(
    text='Режим "Новичек"',
    background="#555",
    foreground="#ccc",
    padx="20",
    pady="8",
    font="20",
    width=20,
    command=RecruitMod
)
btnRec.place(x=847.5, y=260)
btnMatch = Button(
    text='Режим "Продвинутый"',
    background="#555",
    foreground="#ccc",
    padx="20",
    pady="8",
    font="20",
    width=20,
    command=MatchMod
)

btnMatch.place(x=847.5, y=300)

target = Button(
    background="#6797ec",
    foreground="#fff",
    image=image,
    activebackground="#6797ec",
    bd=0,
    command=onTargetClick
)
holst.pack()
holst.mainloop()
