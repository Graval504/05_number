class Successor:
    def __init__(self,n):
        self.prev = n

    def unwrap(self):
        return self.prev

    def __str__(self):
        return("Successor(" + str(self.prev) + ")")

class OneIsNotSuccessor(Exception):
    def __str__(self):
        return "One Is not successor"

	
class NegativeOrZero(Exception):
    def __str__(self):
        return "Natural number is not negative or zero"

def natural(n):
    if n <= 0:
        raise NegativeOrZero()
    elif n == 1:
        return one()
    else:
        result = one()
        for _i in range(n-1):
            result = Successor(result)
        return result
class one(Successor):
    def __init__(self):
        self.prev = None

    def unwrap(self):
        raise OneIsNotSuccessor()
    
    def __str__(self):
        return "1"
    


a = natural(10)
print(a)

