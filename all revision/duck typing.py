class Duck:
    def talk(self):
        print("quack")
class Human:
    def talk(self):
        print('hello')
class livingbeings:
    def howtalk(self,obj):
         obj.talk()
def howtalk1(obj):
        obj.talk()
d=Duck()
h=Human()
l=livingbeings()
l.howtalk(d)
l.howtalk(h)
howtalk1(h)
howtalk1(d)
