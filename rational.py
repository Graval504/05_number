#덧셈 : addition
#뺄셈 : substraction
#곱셈 : multiplication
#나눗셈 : division
#제곱 : power
class Rational:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
        self.simplify()

    def __str__(self):
        num = self.num
        denom = self.denom
        if self.num < 0 and self.denom < 0:
            num = abs(num)
            denom = abs(denom)
        elif self.denom < 0:
            num = -num
            denom = abs(denom)
        return "{}/{}".format(num, denom)
    
    def __add__(self, other):
        s = Rational(1, 1)
        denom1 = abs(self.denom)
        denom2 = abs(other.denom)
        g = gcd(denom1, denom2)
        q1 = int(self.denom / g)
        q2 = int(other.denom / g)
        s.denom = g * q1 * q2
        s.num = self.num * q2 + other.num * q1
        s.simplify()
        return s
    def __mul__(self,other):
        pass
    def __div__(self,other):
        pass
    def __pow__(self,other):
        pass

    def __sub__(self, n):
        pass
    def simplify(self):
        num = abs(self.num)
        denom = abs(self.denom)
        g = gcd(num, denom)
        if g == 1:
            pass
        else:
            self.num = int(self.num / g)
            self.denom = int(self.denom / g)

def gcd(a, b):#유클리드 호제법
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


r1 = Rational(1, 27)

r2 = Rational(2, 27)

print(r1)

print(r2)

print(r1 + r2)

