from  logg import *
def manager():
    f = open('alex.txt', 'r', encoding='utf-8')
    data = eval(f.read())
    print(data)
    info =("""
        ------- 请输入想进行的操作 ---------
        1.  添加账户
        2.  修改用户额度
        3.  冻结账户
      """)
    while 1:
        print(info)
        move = int(input('输入选择的要求'))
        if move == 1:
            logg('添加用户 ')
            name=input('输入添加的用户名')
            password=input('输入此用户名的密码')
            money=int(input('输入对应的金额'))
            log=int(input('输入是否冻结,0为不冻结,1为冻结'))
            account={'name': name, 'password': password, 'money': money, 'log': log}
            f = open('alex.txt', 'w', encoding='utf-8')
            f.write(str(account))
            f.close()

        elif move == 2:
            logg('修改用户额度')
            m=input('输入修改的额度')
            data['money']=m
            f = open('alex.txt', 'w', encoding='utf-8')
            f.write(str(data))
            f.close()

        elif move == 3:
            logg('冻结账户')
            data['log']=1
            f = open('alex.txt', 'w', encoding='utf-8')
            f.write(str(data))
            f.close()
