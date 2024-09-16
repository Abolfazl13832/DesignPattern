from time import sleep


class LazyLoader:
    def __init__(self,cls):
        self.cls = cls
        self.object =None

    def __getattr__(self, item):
        if self.object is None:
            self.object = self.cls()
        return getattr(self.object, item)
    
class M:
    def __init__(self):
        sleep(5)
    def connect(self):
        return "connect mysql"
    
class MO:
    def __init__(self):
        sleep(2)
    def connect(self):
        return "connect MONGO"
    
class N:
    def __init__(self):
        sleep(5)
    def connect(self):
        return "connect notif"
    

m=LazyLoader(M)
mo=LazyLoader(MO)
n=LazyLoader(N)
print(mo.connect())
print(n.connect())

