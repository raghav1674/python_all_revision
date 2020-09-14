# def hello(fun):
#     return fun
# def function():
#     return ("hello")
# # print(hello(function()))
# import time
# def expnum(num):
#     def caltime(func):
#         def timewrapper(num1):
#             start=time.time()
#             print( func(num1,num))
#             end=time.time()
#             print( end-start)
#         return timewrapper
#     return caltime
#
# @expnum(3)
# def anyexp(x,y):
#     return x**y
# print(anyexp(10))


def new(func):
    def h(a,b):
        print("hello",a,b)
        return func(a,b)
    return h

def func(x,y):
    print(x+y)

f=new(func)
f(2,3)





