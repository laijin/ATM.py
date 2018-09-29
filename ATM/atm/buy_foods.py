from action import *
@login
def buy():
    goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
    ]
    print(goods)
    f1=open('foods','r',encoding='utf-8')
    list=eval(f1.read())
    f2 = open('alex.txt', 'r', encoding='utf-8')
    data = eval(f2.read())
    while 1:##进入购买环节
        n = int(input('输入商品编号,必须是数字,按9退出,按0输出购买情况'))
        n-=1
        if 0<=n<4:
            spend=goods[n]['price']
            if data['money']>spend:
                data['money']-=spend
                list['alex']['商品'].append(goods[n]['name'])
                print('\033[32;0m-','商品已加入','-\033[0m')
                print('\033[32;0m-',list['alex'],'-\033[0m')
                print('\033[32;0m-',data['money'],'-\033[0m')
            else:
                print('\033[32;0m\-钱不够-\033[0m ')
        elif n==8:
            print('\033[32;0m-',list['alex'],'-\033[0m')
            print('您的余额','\033[32;0m-',data['money'],'-\033[0m')
            break
        elif n==-1:
            print(list[username])
        else:
            print("必须在1-4之间，或9")
    f = open('foods', 'w',encoding='utf-8')
    f.write(str(list))
    f.close()
    f = open('alex.txt', 'w', encoding='utf-8')
    f.write(str(data))
    f.close()