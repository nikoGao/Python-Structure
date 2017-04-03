from timeit import Timer

def t1():
    l = list(range(1000))
    for i in range(1000):
        l[i] = 1

def t2():
    l = list(range(1000))
    for i in range(1000):
        l.pop(0)

time1 = Timer("t1()", "from __main__ import t1")
time2 = Timer("t2()", "from __main__ import t2")
print(time1.timeit(number=1000))
print(time2.timeit(number=1000))