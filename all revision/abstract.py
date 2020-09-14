from abc import abstractmethod,ABC
class B(ABC):
    @abstractmethod
    def start(self):
        pass
class A(B):
    
    def start(self):
        pass

a=A()
a.start()