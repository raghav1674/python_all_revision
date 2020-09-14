from abc import ABC,abstractmethod
class TouchScreenLaptop(ABC):
    def __init__(self,make):
        self.make=make
    @abstractmethod
    def scroll(self):
        pass
    @abstractmethod
    def click(self):
        pass
class HP(TouchScreenLaptop):
    def __init__(self,model):
        super().__init__("HP")
        self.model=model
    def scroll(self):
        print(self.make,"scrolls")


class Dell(TouchScreenLaptop):
    def __init__(self, model):
        super().__init__("DELL")
        self.model = model

    def scroll(self):
        print(self.make, "scrolls")


class HPNotebook(HP):
    def __init__(self):
        super().__init__("HPNotebook")

    def scroll(self):
        super().scroll()
        print(self.model, "scrolls")
    def click(self):
        print("On",self.model,"we can click")


class DellNotebook(Dell):
    def __init__(self):
        super().__init__("DellNotebook")

    def scroll(self):
        super().scroll()
        print(self.model, "scrolls")

    def click(self):
        print("On", self.model, "we can click")

d=DellNotebook()
d.click()
d.scroll()


h=HPNotebook()
h.scroll()
h.click()


