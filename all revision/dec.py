
def dec(fun):
    def double(x):
        x=2*x
        return(fun(x))
    return double
@dec
def func(x):
    print(x)

func(2)
from functools import wraps
def how_are_you(fn):
    @wraps(fn)
    def inner(n):
        result=fn(n)
        return result+" "+"How are you?"
    return inner
@how_are_you
def hello(name):
    return "Hello"+" "+name.capitalize()+"."

print(hello.__name__)
