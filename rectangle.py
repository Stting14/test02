class Rectangle:
    def __init__(self,width=0,height=0):
        self.width=width
        self.height=height

    def __setattr__(self,name,value):
        if name=='square':
            self.width=value
            self.height=value
        else:
            #self.name=value
            #super().__setattr__(name,value)
            self.__dict__[name]=value

    def getArea(self):
        return self.width * self.height


class CounList:
    def __init__(self,*args):
        self.values=[x for x in args]
        self.count={}.fromkeys(range(len(self.values)),0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self,key):
        self.count[key]+=1
        return self.values[key]
