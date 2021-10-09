import random
from DBUtils import update, select


i = '''
 1
*****以下是你的个人信息******
\t账号：%s
\t姓名：%s
\t密码：******
\t地址：%s
\t余额：%s
\t开户行：%s
'''


# 生成随机8位数字
def random8():
    a = ''
    for n in range(8):
        a += str(random.randint(0, 9))
    return a


def sign_in():
    # 判断输入的余额和密码为数字
    a = True
    b = True
    print('欢迎注册中国工商银行')
    print('已为你自动生成账号，请依次输入下列信息：')
    uid = random8()
    sql1 = 'select * from user where uid = %s'
    args1 = [uid]
    res1 = select(sql1, args1)
    # print(res1)
    sql2 = 'select count(*) 数量 from user'
    res2 = select(sql2, [])
    # print(type(res2[0]['数量']))
    # uid = 11111111
    # 1：成功，2：用户已存在，3：用户库已满
    if res1:
        return 2
    if res2[0]['数量'] > 100:
        return 3
    name = input('请输入您的姓名：')
    while b:
        psw = input('请输入您的密码（6位数字）：')
        if psw.isdigit():
            if len(psw) == 6:
                psw = int(psw)
                b = False
            else:
                print('***请输入6位数字密码***')
        else:
            print('***请输入合法字符***')
    while a:
        money = input('请输入您的余额：')
        if money.isdigit():
            money = int(money)
            a = False
        else:
            print('***请输入合法字符***')
    # address
    print('请完善地址信息')
    nation = input('\t国家：')
    province = input('\t省份：')
    street = input('\t街道：')
    no = input('\t门牌号：')
    address = dict()
    address['国家'] = nation
    address['省份'] = province
    address['街道'] = street
    address['门牌号'] = no
    # info = dict()
    # info['姓名'] = name
    # info['密码'] = psw
    # info['余额'] = money
    # info['地址'] = address
    # info['开户行'] = '工商'
    # userInfos[uid] = info
    sql2 = 'insert into user VALUES(%s,%s,%s,%s,%s,%s,%s,%s,NOW(),%s)'
    args2 = [uid, name, psw, nation, province, street, no, money, '工商']
    update(sql2, args2)
    # print(userInfos)
    return i % (uid, name, address['国家'] + ' ' + address['省份'] + ' ' + address['街道'] + ' ' + address['门牌号'],money, '工商')
