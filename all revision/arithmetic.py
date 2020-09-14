class Arithmetic:
    def __init__(self,x):
        self.x=x
    def __add__(self, other):
        return self.x+other.x
    def __sub__(self, other):
        return self.x - other.x
    def __mul__(self,other):
        return self.x * other.x
    def __radd__(self, other):
        return self.x + other
    def __iadd__(self, other):

        print( self+other)
a=Arithmetic(3)
b=Arithmetic(4)
a+=b