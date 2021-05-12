i = 0
def first():
    global i
    for i in range(10):
        i = i
        print(i)
    print('first', i)





def second():
    global i
    i = 5
    print('second', i)
    first()


first()
second()
