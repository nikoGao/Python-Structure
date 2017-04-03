from Structure.Chapter_3.Stack import Stack
# function of int(x, 2) and bin()

def divideBy2(x):
    s = Stack()
    while x:
        x, res = divmod(x, 2)
        s.push(res)
    two_res = ''
    while not s.isEmpty():
        two_res += str(s.pop())
    return two_res

def baseConverter(nums, base):
    digits = "0123456789ABCDEF"
    s = Stack()
    while nums:
        nums, ret = divmod(nums, base)
        s.push(ret)
    res = ''
    while not s.isEmpty():
        res += digits[s.pop()]
    return res

print(baseConverter(25,8))
print(baseConverter(256,16))