
class test:
    def __new__(cls):
        print('新生成一个对象')
        return super(test,cls).__new__(cls)

    @staticmethod
    def t():
        print('!')

test()

##super(test,self)  表示把本类的self 转化为 父类的一个self（对象） 注意type元类的对象是类
