from DBUtils import update, select


def save_money():
    """根据传的账号account和存取金额count存钱"""
    print('======存钱======')
    account = input('请输入您的账号：')
    psw = input('请输入您的密码：')
    sql1 = 'select * from user where uid = %s and password = %s'
    args1 = [account, psw]
    res1 = select(sql1, args1)
    if res1:

        count = int(input('请输入存取的金额：'))
        sql2 = 'update user set money = money + %s where uid = %s and password = %s'
        args2 = [count, account, psw]
        update(sql2, args2)
        return True
    else:
        print('账号或密码不正确')
        return False


def withdraw_money():
    print('======取钱======')
    """0：正常，1：账号不存在，2：密码不对，3：钱不够"""
    account = input('请输入您的账号：')
    psw = int(input('请输入您的密码：'))
    sql3 = 'select * from user where uid = %s'
    args3 = [account]
    res3 = select(sql3, args3)
    if res3:
        if psw == res3[0]['password']:
            count = int(input('请输入要取的金额：'))
            if res3[0]['money'] >= count:
                sql4 = 'update user set money = money - %s where uid = %s and password = %s'
                args4 = [count, account, psw]
                update(sql4, args4)
                print('取钱成功')
                return 0
            else:
                print('余额不足')
                return 3
        else:
            print('密码不正确')
            return 2
    else:
        print('账号不存在')
        return 1


def move_money():
    """0：正常，1：账号不对，2密码不对，3钱不够"""
    print('======转账======')
    out_account = input('请输入转出账号：')
    in_account = input('请输入转入账号：')

    sql5 = 'select * from user where uid = %s'
    args5 = [out_account]
    res5 = select(sql5, args5)   # 出
    sql6 = 'select * from user where uid = %s'
    args6 = [in_account]
    res6 = select(sql6, args6)   # 入

    if res6 and res5 and out_account != in_account:
        out_psw = int(input('请输入转出账号的密码：'))
        if out_psw == res5[0]['password']:
            money = int(input('请输入转出金额：'))
            if res5[0]['money'] >= money:
                sql7 = 'update user set money = money - %s where uid = %s and password = %s'
                sql8 = 'update user set money = money + %s where uid = %s'
                args7 = [money, out_account, out_psw]
                args8 = [money, in_account]
                update(sql7, args7)
                update(sql8, args8)
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1


def query():
    print('======查询======')
    account = input('请输入您的账号：')
    sql9 = 'select * from user where uid = %s'
    args9 = [account]
    res9 = select(sql9, args9)
    if res9:
        psw = int(input('请输入您的密码：'))
        if psw == res9[0]['password']:
            print(f'''
            当前账号：{account}
            姓名：{res9[0]['name']}
            密码：******
            余额：{res9[0]['money']}元
            用户居住地址：{res9[0]['country'] + res9[0]['province'] + res9[0]['street'] + res9[0]['door']}
            当前账号的开户行：{res9[0]['bank']}
            ''')
        else:
            print('密码错误')
    else:
        print('当前用户不存在')
