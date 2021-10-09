# 如何能在python中去使用mysql数据库存取数据?    使用pymysql模块
import pymysql


def update(sql, args):
    # 创建链接得到一个链接对象
    con = pymysql.connect(
        host='localhost',  # 数据库服务器本机地址
        user='root',  # 用户名
        password='111111',  # 密码
        database='bank'  # 要连接的数据库
    )
    cursor = con.cursor()
    cursor.execute(sql, args)
    con.commit()

    # 关闭链接
    cursor.close()
    con.close()


def select(sql, args, mode='all', size=1):
    # 创建链接得到一个链接对象
    con = pymysql.connect(
        host='localhost',  # 数据库服务器本机地址
        user='root',  # 用户名
        password='111111',  # 密码
        database='bank'  # 要连接的数据库
    )
    cursor = con.cursor(pymysql.cursors.DictCursor)
    res = cursor.execute(sql, args)
    if mode == 'all':
        return cursor.fetchall()
    elif mode == 'one':
        return cursor.fetchone()
    elif mode == 'many':
        return cursor.fetchmany(size)
    con.commit()

    # 关闭链接
    cursor.close()
    con.close()


