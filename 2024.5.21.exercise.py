# 列表练习
"""
def change_number(my_list, place, num):
    del my_list[place - 1]
    my_list.insert(place - 1, num)
    return None

my_list = []
for i in range(10):
    my_list.append(i+1)
print(my_list)
my_list.insert(0, 0)
print(my_list)
print(len(my_list))
print(my_list.index(5))
del my_list[4]
print(my_list)
place = int(input("请输入你要改的元素位置"))
num = int(input("请输入你要将其改为什么"))
change_number(my_list, place, num)
print(my_list)
print(my_list.count(0))
"""
"""
my_list = [1, 2, 3, 4, 5]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
"""

# 列表练习
"""
def mainnenu():
    print("\t\t\t欢迎使用列表操作系统")
    print("\t\t\t  1.打印列表元素")
    print("\t\t\t  2.获得指定元素")
    print("\t\t\t  3.插 入 元 素")
    print("\t\t\t  4.删 除 元 素")
    print("\t\t\t  5.查 找 元 素")
    print("\t\t\t  6.修 改 元 素")
    print("\t\t\t  7.统计出现次数")
    print("\t\t\t  8.统计列表长度")
    print("\t\t\t  9.列 表 延 长")
    print("\t\t\t  0.退 出 系 统")
    print("请选择操作-->")
    return None

print("请创建一个列表")
my_list = []
n = int(input("请输入列表中的元素个数"))
for i in range(n):
    element = int(input(f"请输入第{i+1}个元素"))
    my_list.append(element)
print("列表创建成功")
flag = True
while flag:
    mainnenu()
    choice = int(input())
    if choice == 1:
        print(my_list)
    elif choice == 2:
        result = int(input("输入你想要得到元素的下标"))
        number = my_list[result]
        print(f"成功得到元素,它是{number},其下标是{result}")
    elif choice == 3:
        num = int(input("请输入你想要插入的元素"))
        place = int(input("请输入你想要插入的位置"))
        my_list.insert(place,num)
        print("成功插入")
        print(my_list)
    elif choice == 4:
        place = int(input("请输入你想要删除的元素的位置"))
        del my_list[place - 1]
        print("删除成功")
    elif choice == 5:
        index = int(input("请输入你想要查找的元素"))
        num = my_list.index(index)
        if num == None:
            print("无法找到,请重新输入")
        else:
            print("成功得到该元素，其下标为%d" % num)
    elif choice == 6:
        num = int(input("请输入你要修改的元素值"))
        place = int(input("请输入你想要修改的位置"))
        del my_list[place]
        my_list.insert(place, num)
        print("修改成功")
        print(my_list)
    elif choice == 7:
        num  = int(input("请输入要统计的元素"))
        print(f"{num}一共出现了{my_list.count(num)}次")
    elif choice == 8:
        print("列表现在的长度是%d" % (len(my_list)))
    elif choice == 9:
        new_list = []
        length = int(input("你想要延长的列表的长度是?"))
        for i in range(length):
            num = int(input("请输入第%d个元素" % (i + 1)))
            new_list.append(num)
        my_list.extend(new_list)
        print("延长成功")
        print(my_list)
    elif choice == 0:
        flag =False
        print("感谢使用系统，程序退出")
    else:
        print("选择错误，请重新选择")
"""
"""
my_list = []
for i in range(3):
    for j in range(3):
        new_list = []
        num = int(input("请输入"))
        new_list.append(num)
        my_list.extend(new_list)
for i in range(1, 10):
    print("%d " % (my_list[i-1]), end=" ")
    if i % 3 == 0:
        print("\n")
"""
"""
# 元组练习
t1 = (1, 2, 3, 4, 5)
print(t1)
t2 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(t1[1])
t3 = ([1,2,3], (4, 5, 6), (4, 5, 7))
t3[0][2] = 2
place = t1.index(5)
print(place)
print(t1.count(4))
print(len(t3))
count = 0
while count < len(t1):
    print(f"元素是{t1[count]}")
    count += 1
for i in range(len(t1)):
    print(f"元素是{t1[i]}")
"""
s = "zxl"
print(s[0])
print(s[1])
print(s[2])



















