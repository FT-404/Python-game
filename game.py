from tkinter import *
from time import *
from random import *

root = Tk()
image = PhotoImage(file="bird2.png")
image2 = PhotoImage(file="anim.png")
bg = PhotoImage(file="bg.png")
root.title('Игра про птичек')
root.geometry('1920x1080')
root.configure(background='#fff')
root.config(cursor='tcross')
holst = Label(root, width=1920, height=1080, highlightbackground="#fff", image=bg)

# img = Image.open("bg2.jpg")
# holst.img = ImageTk.PhotoImage(img)
# holst['image'] = holst.img

lab = Label(bg='#6797ec', font="20")
gameTimerLab = Label(bg='#6797ec', font='40')
counter = Label(bg='#6797ec', font="20")

lives = 3
flag = 0
count = 0
bossCount = 0
ff = 0
bosser = 1


def Starter():
    lab.place(x=950, y=20)
    counter.place_forget()
    backTimer = 4
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
        backTimer = ''
        lab.config(text=str(backTimer))
        onTargetClick()
        root.update()
        counter.config(text='Счёт: ' + str(count))
        global lives
        if lives == 0:
            lives = 1
            target.place_forget()
            if count % 10 == 1:
                ans = ' очко!'
            elif count % 10 >= 2 and count % 10 <= 4:
                ans = ' очка!'
            else:
                ans = ' очков!'
        counter.config(text='Вы набрали - ' + str(count) + ans)
        counter.place(x=890, y=70)
        btnRec.place(x=847.5, y=260)
        btnMatch.place(x=847.5, y=300)


def koordX(first, second):
    x = uniform(first, second)
    return x


def koordY():
    y = randint(90, 460)
    return y


def onTargetClick():
    global lives, flag, count, image, image2, ff, bosser

    y = koordY()
    if ff == 10 * bosser - 1:

        image = PhotoImage(file="i.png")
        image2 = PhotoImage(file="i.png")
        ff += 1
        bosser += 1

        onTargetClick()
    else:
        x = koordX(0.25, 0.75)
        print('bosser:', 10 * (bosser - 1) - 1, '\n count: ', count)

        if count == 10 * (bosser - 1) - 1 and count != -1:

            x = koordX(0.1, 0.18)

        if count == ff:
            image = PhotoImage(file="bird2.png")
            image2 = PhotoImage(file="anim.png")
        if flag == 0:
            count += 1
            ff = count
            counter.config(text='Счёт: ' + str(count))

        k = 50

        for i in range(1920):
            target.place(x=i / x, y=y)
            if int(target.place_info().get('x')) > k and int(target.place_info().get('x')) < k + 50:
                target.config(image=image2)

            elif int(target.place_info().get('x')) > k + 50 and int(target.place_info().get('x')) < k + 100:
                target.config(image=image)
                k += 100

            if int(target.place_info().get('x')) >= 1920:
                lives -= 1
                flag = 1

                onTargetClick()
            else:
                flag = 0
            root.update()
            if lives <= 0:
                target.place_forget()
                break


def RecruitMod():
    global count, lives
    count -= 1
    Starter()


def MatchMod():
    global count
    count = -1
    Starter()


btnRec = Button(
    text='Режим "Тренировка"',
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
    text='Режим "Соревновательный"',
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
holst.place(x=0, y=0)
holst.mainloop()
