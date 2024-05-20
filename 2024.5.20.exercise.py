# 乘法表

"""
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d=%2d "%(j, i, i*j),end=" ")
    print("\n")
"""

# 交换数字
'''
def swap(a, b):
    temp = b
    b = a
    a = temp
    print(a," ",b)
a = int(input())
b = int(input())
swap(a, b)
print(a)
print(b)
'''

# 猜数字
"""
import random
random_number = random.randint(1, 10)
count = 0
flag = False
while count < 3:
    count += 1
    number = int(input("请猜数字"))
    if number > random_number:
        print("猜大了")
    elif number < random_number:
        print("猜小了")
    else:
        print("恭喜你,猜对了")
        flag = True
        break
if not flag:
    print("很遗憾,你没有猜对数字")
"""
'''
a = '"a"'
print(a)
b = "\"b\""
print(b)
c = """\"c\""""
print(c)
'''
"""
def check():
    print("请出示你的码")

for i in range(10):
    check()
"""
'''
def add (x, y):
    return x + y
print("%d" % add(1, 2))
'''
'''
num = 100
def displaynum ():
    print(num)
def changenum ():
    global num
    num = 500
displaynum()
changenum()
print(num)
'''
'''
money = 50000
def mainmenu(name):
    print(name + "你好,欢迎来到ATM")
    print("\t1.查询余额")
    print("\t2.存款")
    print("\t3.取款")
    print("\t0.退出")
    print("\t请选择您的操作->", end=" ")
    return None

def check_moeny(name):
    global money
    print(f"{name},您好,你余额还剩{money}")

def save_money(name, in_money):
    global money
    money += in_money
    print(f"{name},您好,您存款{in_money}成功")
    check_moeny(name)

def take_money(name, out_money):
    global money
    flag = money - out_money
    if flag < 0:
        print("操作失败，余额不足")
        return None
    money -= out_money
    print(f"{name},您好,您取款{out_money}成功")
    check_moeny(name)


name = input("尊敬的用户，请输入你的名字")
ID = input("请输入你的卡号")
flag = True
while flag:
    mainmenu(name)
    choice = int(input())
    if choice == 1:
        check_moeny(name)
    elif choice == 2:
        in_money = int(input("请输入您要存款的金额"))
        save_money(name, in_money)
    elif choice == 3:
        out_money = int(input("请输入您要取款的金额"))
        take_money(name,out_money)
    elif choice == 0:
        flag = False
        print("欢迎使用，程序退出")
    else:
        print("选择错误，请重新选择")
'''
'''
my_list = []
for i in range(10):
    num = int(input("请输入第%d个元素" % (i+1)))
    my_list.append(num)
print(my_list)
'''
'''
my_list = []
for i in range(10):
    my_list.append(i + 1)
print(my_list)
for i in range(10):
    print(my_list.pop())
'''


'''
my_list = []
# 初始化
for i in range(10):
    my_list.append(i + 1)

my_list.insert(0, 0)
print(my_list)
del my_list[0]
print(my_list)
my_list.pop(2)
print(my_list)
my_list.remove(4)
print(my_list)
external_list = [11, 12, 13]
my_list.extend(external_list)
print(my_list)
index = my_list.index(5)
print(index)
count = my_list.count(1)
print(count)
length = len(my_list)
print(length)
'''
# 列表练习
# 函数准备
def main_menu ():
    print("\t\t请选择你的操作")
    print("\t\t 1.输出列表")
    print("\t\t 2.插入元素")
    print("\t\t 3.删除元素")
    print("\t\t 4.查找元素")
    print("\t\t 5.统计长度")
    print("\t\t 6.取出元素")
    print("\t\t 0.退出系统")
    return None

def arrinsert(arr, key, place):
    arr.insert(place, key)
    return None

def delarr(arr, place):
    del arr[place]
    return None

def searcharr(arr, key):
    return arr.index(key)


# 初始化列表
print("请创建一个列表")
arr = []
n = int(input("列表中有几个元素?"))
for i in range(n):
    num = int(input("请输入第%d个元素" % (i + 1)))
    arr.append(num)
flag = True
while flag:
    main_menu()
    choice = int(input("请选择你的操作"))
    if choice == 1:
        print(arr)
    elif choice == 2:
        key = int(input("请输入你要插入的元素"))
        place = int(input("请选择你要插入的位置"))
        arrinsert(arr, key, place)
    elif choice == 3:
        place = int(input("请输入你要删除元素的下标"))
        delarr(arr, place)
    elif choice == 4:
        key = int(input("请输入要查找的元素"))
        place = searcharr(arr, key)
        if place:
            print("成功找到，下标是%d" % place)
        else:
            print("无法找到，请重新确认")
    elif choice == 5:
        length = len(arr)
        print(f"列表目前的长度是{length}")
    elif choice == 6:
        place = int(input("请选择你要取出的元素的下标"))
        result = arr.pop(place)
        print("取出的元素是%d" % result)
        print("现在表中的元素还剩:")
        print(arr)
    elif choice == 0:
        flag = False
        print("感谢使用列表操作系统，程序退出")
    else:
        print("选择错误，请重新选择")

















