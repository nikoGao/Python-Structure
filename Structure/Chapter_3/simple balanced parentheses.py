from Structure.Chapter_3 import Stack
# Use stack to verify whether parentheses is valid,
# Can be used in Leetcode 20, 22
__author__ = 'Niko'


def isMatch(s, top):
    if s == ')':
        return top == '('
    if s == '}':
        return top == '{'
    if s == ']':
        return top == '['

def parChecker(symbolString):
    s = Stack.Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        if symbolString[index] in '([{':
            s.push(symbolString[index])
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not isMatch(symbolString[index], top):
                    balanced = False
        index += 1
    if s.isEmpty() and balanced:
        return True
    return False

if __name__ == '__main__':
    print(parChecker('{{([][])}()}'))
    print(parChecker('[{()]'))