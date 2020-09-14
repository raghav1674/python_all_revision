class car:
    def __init__(self,num):
        self.e=self.Engine(num)

    class Engine:
        def __init__(self,number):
            self.number=number
        def hello(self):
            print("hello")

c=car(123)
c.e.hello()

e1=c.Engine(123)
e1.hello()
