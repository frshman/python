class Test1:
    name = 'll'
    age = '18'

    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)

    def pf(self):
        self.x = 1
        print(self.name)
        print(self.__dict__)
        print(self.sex)
        print(self.x)
    

t1 = Test1(sex = 'famale',fun = lambda x:x+1)
t1.pf()
print(t1.fun(1))

# from rest_framework.generics import GenericAPIView