class Dequeue:
    def __init__(self):
        self.deque = []

    def addFront(self, x):
        self.deque.insert(0, x)

    def addRear(self, x):
        self.deque.append(x)

    def removeFront(self):
        if not self.isEmpty():
            return self.deque.pop(0)

    def removeRear(self):
        if not self.isEmpty():
            return self.deque.pop()

    def isEmpty(self):
        if len(self.deque) == 0:
            return True
        return False

    def size(self):
        return len(self.deque)