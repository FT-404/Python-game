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
gameTimerLab = Label(bg='#fff', font='40')
gameTimerLab.pack()
counter = Label(bg='#fff', font="20")
counter.pack()


def Starter():
    global backTimer
    backTimer = 4
    gameTimer = 10
    btnRec.pack_forget()
    btnMatch.pack_forget()

    for x in range(4):
        backTimer -= 1
        if x == 3:
            backTimer = 'Start!'
        lab.config(text=str(backTimer))
        sleep(1)
        root.update()
    if backTimer == 'Start!':
        sleep(1)
        timing = time()
        lab.destroy()
        target.place(x=koordX(), y=koordY())
        root.update()
        counter.config(text='Счёт: ' + str(0))
        while gameTimer != 0:
            if time() - timing > 1:
                timing = time()
                gameTimer -= 1
                print(gameTimer)
            gameTimerLab.config(text='Оставшееся время: ' + str(gameTimer))
            root.update()

        if gameTimer == 0:
            gameTimerLab.destroy()
            target.destroy()
            btnRec.pack()
            btnMatch.pack()
            if count == 1:
                ans = ' очко!'
            elif count >= 2 and count <= 4:
                ans = ' очка!'
            else:
                ans = ' очков!'
            counter.config(text='Вы набрали - ' + str(count) + ans)



def koordX():
    x = randint(0, 1800)
    return x


def koordY():
    y = randint(0, 960)
    return y


def RecruitMod():
    Starter()


count = 0


def onTargetClick():
    global count
    count += 1
    counter.config(text='Счёт: ' + str(count))
    target.place(x=koordX(), y=koordY())


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
btnRec.pack()
btnMatch = Button(
    text='Режим "Продвинутый"',
    background="#555",
    foreground="#ccc",
    padx="20",
    pady="8",
    font="20",
    width=20
)

btnMatch.pack()
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
