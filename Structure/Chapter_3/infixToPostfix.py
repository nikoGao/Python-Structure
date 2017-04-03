from Structure.Chapter_3.Stack import Stack

def infixToPostfix(forum):
    prec = {'*':3, '/':3, '+':2, '-': 2, '(':1, '^':4}
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
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[token]:
                oparend.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        oparend.append(opStack.pop())
    return ''.join(oparend)


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token.isdigit():
            operandStack.push(token)
        else:
            operand2 = int(operandStack.pop())
            operand1 = int(operandStack.pop())
            result = doMath(operand1, operand2, token)
            operandStack.push(result)
    return operandStack.pop()


def doMath(operand1, operand2, token):
    if token == '+':
        return operand1 + operand2
    if token == '-':
        return operand1 - operand2
    if token == '*':
        return operand1 * operand2
    if token == '/':
        return operand1 / operand2

print(infixToPostfix("5 * 3 ^ ( 4 - 2 )"))
