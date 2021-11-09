# 测试python中下划线的命名规则

class Test:
    def __init__(self) -> None:
        self._user = 'll'
        self.__user_password = 123

test1 = Test()
try:
    print(test1.__user_password)
    print(test1._user)
except Exception as e:
    print(e)

# 'Test' object has no attribute '__user_password'
# result
# 单下划线_ 只是python约定俗成的写法，表示我不想让人访问，修改该属性或者方法，但是实际上可以直接访问
# 双下划线 __ 采用了命名规则 ，对于__obj,python解释器会自动将其变成_classname__obj,防止子类重复定义，直接访问就会报错。
