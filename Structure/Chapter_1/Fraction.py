def gcd(m, n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        if self.num == 0:
            return '0'
        if self.den == 1:
            return str(self.num)
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        newnum = self.num*other.den + self.den*other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum/common, newden/common)

    def __sub__(self, other):
        newnum = self.num*other.den - self.den *other.num
        newden = self.den*other.den
        common = gcd(newnum, newden)
        return Fraction(newnum/common, newden/common)

    def __mul__(self, other):
        newnum = self.num*other.num
        newden = self.den*other.den
        common = gcd(newnum, newden)
        return Fraction(newnum/common, newden/common)

    def __div__(self, other):
        newnum = self.num*other.den
        newden = self.den*other.num
        common = gcd(newnum, newden)
        return Fraction(newnum / common, newden / common)

    def __eq__(self, other):
        firstnum = self.num*other.den
        secondnum = self.den*other.num
        return firstnum == secondnum

if __name__ == '__main__':
    num1 = Fraction(1,4)
    num2 = Fraction(1,8)
    print num1/num2

