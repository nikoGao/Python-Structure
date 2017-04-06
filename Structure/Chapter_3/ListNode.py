class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def getData(self):
        return self.val

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.val = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        curr = self.head
        count = 0
        while curr != None:
            count += 1
            curr = curr.getNext()
        return count

    def search(self, target):
        curr = self.head
        while curr != None:
            if curr.getData() == target:
                return True
            curr = curr.getNext()

        return False

    def remove(self, item):
        prev, curr = None, self.head
        found = False
        while not found:
            if curr.getData() == item:
                found = True
            else:
                prev = curr
                curr = curr.getNext()
        "prev==None means that item is the first in the list"
        if not prev:
            self.head = curr.getNext()
        else:
            prev.setNext(curr.getNext())

    def append(self, item):
        curr = self.head
        while curr.getNext() != None:
            curr = curr.getNext()
        temp = Node(item)
        temp.setNext(curr.getNext())
        curr.setNext(temp)

    def insert(self, index, item):
        curr = self.head
        pos = 0
        while pos < index:
            curr = curr.getNext()
            pos += 1
        if curr != None:
            temp = Node(item)
            temp.setNext(curr.getNext())
            curr.setNext(temp)
        else:
            print("index out of range")

    def getItem(self, index):
        curr = self.head
        pos = 0
        while pos < index:
            curr = curr.getNext()
            pos += 1
        if curr != None:
            return curr.getData()
        else:
            print("index out of range")

    def pop(self, index):
        return self.remove(self.getItem(index))


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        previous = None
        curr = self.head
        while curr != None and curr.getData() < item:
            previous = curr
            curr = curr.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            previous.setNext(temp)
            temp.setNext(curr)

    def size(self):
        curr = self.head
        count = 0
        while curr != None:
            count += 1
            curr = curr.getNext()
        return count

    def search(self, target):
        curr = self.head
        while curr != None:
            if curr.getData() == target:
                return True
            elif curr.getData() > target:
                break
            curr = curr.getNext()
        return False

    def remove(self, item):
        prev, curr = None, self.head
        found = False
        while not found:
            if curr.getData() == item:
                found = True
            else:
                prev = curr
                curr = curr.getNext()
        "prev==None means that item is the first in the list"
        if not prev:
            self.head = curr.getNext()
        else:
            prev.setNext(curr.getNext())

mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
