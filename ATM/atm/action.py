from manager import *
user_status = False
def login(fun):
    def inner(*args, **kwargs):  # 可变参数
        _username = "alex"
        _password = "123"
        _managername = 'peiqi'
        _managerword = '321'
        global user_status
        if user_status == False:
            username = input("用户名:")
            password = input("密码:")
            if username == _username and password == _password:
                print("欢迎....")
                user_status = True
            elif username == _managername and password == _managerword:
                print("欢迎管理者...")
                user_status = True
                manager()
            else:
                print("输入有误")
        if user_status == True:
            fun(*args, **kwargs)
    return inner

@login
def output():
    f = open('alex.txt', 'r', encoding='utf-8')
    data = eval(f.read())
    f.close()
    print('账户余额', data['money'])
    print('name', data['name'])

@login
def transfer():
    f1 = open('alex.txt', 'r', encoding='utf-8')
    data1 = eval(f1.read())
    f2 = open('peiqi.txt', 'r',encoding='utf-8')
    data2 = eval(f2.read())
    m=input('请输入要转账的金额给peiqi：')
    m=int(m)
    print(type(data1['money']))
    data1['money']=data1['money']-m
    data2['money']=data2['money']+m
    print(data1['money'],data2['money'])
    print('转账给了peiqi,花费了', m)

    print('余额剩下', data1['money'])
    f1.close()
    f2.close()

@login
def takeout():
    withdraw_price = input('请输入提现金额>')
    withdraw_price = int(withdraw_price)

    f = open('alex.txt', 'r')
    data = eval(f.read())
    print(data)
    if data['log'] == 0:
        cost_price = withdraw_price * 1.05
        print('取出了', withdraw_price)
        data['money'] -= cost_price
        print('减少',cost_price)
        f = open('alex.txt', 'w',encoding='utf-8')
        f.write(str(data))
        f.close()

@login
def pay():
    pay_price = input('请输入还款金额>')
    pay_price = int(pay_price)

    f = open('alex.txt', 'r')
    data = eval(f.read())
    print('还款',pay_price)
    data['money']+=pay_price
    f = open('alex.txt', 'w', encoding='utf-8')
    f.write(str(data))
    f.close()
