from logg import *
from action import *
from buy_foods import *
def main():
    msg = """
        ------- Luffy Bank ---------
        1.  账户信息
        2.  转账
        3.  提现
        4.  还款
        5.  进入购物环节
      """
    while 1:
        print(msg)
        logg('开始 ... ')
        logg('菜单')
        choice = int(input('输入选择的要求'))
        logg('进入')

        if choice == 1:
            logg('账户余额 ')
            output()

        elif choice == 2:
            logg('转账 ')
            transfer()

        elif choice == 3:
            # from takeout import *
            logg('提现')
            takeout()

        elif choice == 4:
            logg('还款')
            pay()

        elif choice == 5:
            logg('进入商品购买环节')
            buy()


if __name__ == '__main__':
    main()