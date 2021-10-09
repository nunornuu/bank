from sign_in import sign_in
from money import save_money, withdraw_money, move_money, query


# 退出系统变量
e = True
# 存储数据


print('***************************')
print('**\t\t中国工商银行\t\t **')
print('**\t\t账户管理系统\t\t **')
print('***************************')
print('\n*\t1.开户\t\t\t\t  *')
print('*\t2.存钱\t\t\t\t  *')
print('*\t3.取钱\t\t\t\t  *')
print('*\t4.转账\t\t\t\t  *')
print('*\t5.查询\t\t\t\t  *')
print('*\t6.Bye！\t\t\t\t  *')
print('***************************')

while e:
    a = input('请输入要办理的业务：')
    if a == '开户' or a == '1':
        b = sign_in()
        print(b)
        # print(userInfos)
    elif a == '存钱' or a == '2':
        b = save_money()
        print(b)
        # print(userInfos[account]['余额'])
    elif a == '取钱' or a == '3':
        b = withdraw_money()
        print(b)
    elif a == '转账' or a == '4':
        b = move_money()
        print(b)
    elif a == '查询' or a == '5':
        query()
    elif a == 'Bye!' or a == '6':
        print('欢迎下次光临')
        break
    else:
        print('该业务不存在')
