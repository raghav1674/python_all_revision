class Square:
    def __init__(self,max):
        self.max=max
        self.current=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.max:
            result=self.current**2
            self.current+=1
            return result


        else:
            raise StopIteration

s1=Square(10)
y=iter(s1)
for i in y:
    print(i)