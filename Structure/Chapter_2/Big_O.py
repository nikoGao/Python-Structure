__author__ = 'nagao'
def FindMiniNum(l):
    mini = l[0]
    for i in range(len(l)):
        if l[i] < mini:
            mini = l[i]
    return mini

print (FindMiniNum([5,2,4,1]))

def CompareString(s1, s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in s1:
        pops = ord(i)-ord('a')
        c1[pops] += 1

    for i in s2:
        pops = ord(i) - ord('a')
        c2[pops] += 1

    return c1 == c2

print(CompareString('abc', 'bac'))