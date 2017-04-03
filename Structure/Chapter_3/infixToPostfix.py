from Structure.Chapter_3.Stack import Stack

def infixToPostfix(forum):
    prec = {'*':3, '/':3, '+':2, '-': 2, '(':1}
    opStack = Stack()
    oparend = []
    tokenlist = forum.split()
    for token in tokenlist:
        if token.isdigit() or token.isalpha():
            oparend.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                oparend.append(topToken)
                topToken = opStack.pop()
        else:
            while not opStack.isEmpty() and prec[opStack.peek()] > prec[token]:
                oparend.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        oparend.append(opStack.pop())
    return ''.join(elem for elem in oparend)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))