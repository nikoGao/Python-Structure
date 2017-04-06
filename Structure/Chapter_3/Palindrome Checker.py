# Can be connected with all palindrome in leetcode

from Structure.Chapter_3.Dequeue import Dequeue


def palchecker(aString):
    paldeque = Dequeue()
    for letter in aString:
        paldeque.addRear(letter)

    while not paldeque.isEmpty() and paldeque.size() > 1:
        front = paldeque.removeFront()
        back = paldeque.removeRear()
        if front != back:
            return False
    return True

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))