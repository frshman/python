
import pymysql

class mysql:
    def __init__(self, host="localhost", port=3306, db="", user="root", passwd="root", charset="utf8"):
        
        # 创建数据库连接
        self.dbconn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        
        # 创建字典型游标(返回的数据是字典类型)
        self.dbcur = self.dbconn.cursor(cursor = pymysql.cursors.DictCursor)

    def __enter__(self):
        
        return self.dbcur

    def __exit__(self, exc_type, exc_value, exc_trace):
    
        # 提交事务
        self.dbconn.commit()
        
        # 关闭游标
        self.dbcur.close()
        
        # 关闭数据库连接
        self.dbconn.close()


if __name__ == "__main__":
    #这里的db就是__enter__中return的对象
    with mysql(db='爬虫') as db:
        sql = 'select * from ftx'
        db.execute(sql)
        print(db)
        for i in db:
            print(i)
