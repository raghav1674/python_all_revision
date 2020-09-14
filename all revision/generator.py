def fibonacci(x):
    '''this will calculate the fibonacci series upto the value specified'''
    a, b = 0, 1
    i=1
    while i<=x:

        yield a
        a,b=b,a+b
        i+=1


def factorial(x):
    '''this will calclulate the factorial series upto the value specified'''
    i=1
    while i<=x+1:
        j = 1
        a = 1
        while j<=i:
            a=a*j
            j+=1
        yield str(i)+"!="+str(a)
        i+=1


def myrange(x,y,z=1):
   '''this will calculate the range upto the given range syntax: myrange(start,stop,step)'''
   while x<=y:
        yield x
        x+=z




if __name__=="__main__":
    print("MYRANGE:")
    for i in myrange(2, 10, 2):
        print(i)

    print()
    print("myfactorial:")

    for i in factorial(6):
        print(i)
    print()
    print("myfibonacci:")
    for i in fibonacci(10):
        print(i)