from tkinter import *
from time import *
from random import *
from PIL import Image, ImageTk

root = Tk()
image = PhotoImage(file="bird2.png")
image2 = PhotoImage(file="anim.png")
root.title('Прямоугольник зеленый')
root.geometry('1920x1080')
root.configure(background='#fff')
root.config(cursor='tcross')
holst = Label(root, width=1920, height=1080, highlightbackground="#fff")
img = Image.open("bg2.jpg")
holst.img = ImageTk.PhotoImage(img)
holst['image'] = holst.img
lab = Label(bg='#6797ec', font="20")
count = 0
gameTimerLab = Label(bg='#6797ec', font='40')
counter = Label(bg='#6797ec', font="20")
lives = 1
flag = 0


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
        timing = time()
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


def koordX():
    x = uniform(0.25, 0.75)
    return x


def koordY():
    y = randint(90, 460)
    return y


def onTargetClick():
    global lives, flag, count, image
    if flag == 0:
        count += 1
        counter.config(text='Счёт: ' + str(count))
    x = koordX()
    y = koordY()
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
    global count
    count -= 1
    Starter()


def MatchMod():
    global count
    count = -1
    Starter()


btnRec = Button(
    text='Режим "Новичок"',
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
