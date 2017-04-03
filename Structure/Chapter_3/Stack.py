class Stack():
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.isEmpty():
           return  self.stack.pop()

    def isEmpty(self):
        if len(self.stack):
            return False
        return True

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None

    def size(self):
        return len(self.stack)

def revString(string):
    s = Stack()
    res = ''
    for each in string:
        s.push(each)
    for i in range(s.size()):
        res += s.pop()
    return res

if __name__ == '__main__':
    print(revString('Hello World!'))
