global c
def fun1(a, b):
    global c
    b = 2
    print('a:', a)
    print('c:', b)


fun1(1, c)