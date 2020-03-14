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
            num = -1 * num
            denom = abs(denom)
        return "{}/{}".format(num, denom)
    
    def __add__(self, other):
        r(self)
        r(other)
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
        r(self)
        r(other)
        s = Rational(self.num * other.num ,self.denom * other.denom)
        s.simplify()
        return s
    def __truediv__(self,other):
        r(self)
        r(other)
        s = Rational(self.num * other.denom ,self.denom * other.num)
        s.simplify()
        return s
    def __pow__(self,other):
        s = Rational(self.num ** other,self.denom**other)
        s.simplify()
        return s
    def __sub__(self, other):
        r(self)
        r(other)
        s = Rational(1, 1)
        denom1 = abs(self.denom)
        denom2 = abs(other.denom)
        g = gcd(denom1, denom2)
        q1 = int(self.denom / g)
        q2 = int(other.denom / g)
        s.denom = g * q1 * q2
        s.num = self.num * q2 - other.num * q1
        s.simplify()
        return s
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
def r(other):
    try:
        if other.num == other.num:
            pass
    except:
        other = Rational(other,1)
        return other

r1 = Rational(3, 2)
r2 = Rational(1, 4)
print("r1", r1)
print("r2", r2)
print()
 
print("r1+r2=", r1 + r2)
print("r1-r2=", r1 - r2)
print("r1*r2=", r1 * r2)
print("r1/r2=", r1 / r2)
print("r1**2=", r1 ** 2)
