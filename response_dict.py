class response_dic:
    '''
    写web接口的时候，每次都要写一个返回的字典，比较麻烦，
    直接封装成一个类，下次直接调用即可，修改也方便
    '''
    def __init__(self) -> None:
        self.status = 100
        self.msg = '成功'

    @property
    def get_dict(self):
        return self.__dict__

if __name__ == '__main__':
    dict_obj = response_dic()
    print(dict_obj.get_dict)
    #{'status': 100, 'msg': '成功'}