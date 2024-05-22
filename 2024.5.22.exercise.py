"""
my_str = "  ABCDefghijk  $ "
for i in range(len(my_str)):
    print(f"第{i+1}个元素是{my_str[i]}")
place = my_str.index("A")
print(f"\"A\"的下标是{place}")
s1 = input("请输入你想要的串")
print(s1)
"""
# 字符串练习
"""
my_str = "itheima itcast boxuage"
count = my_str.count("it")
s2 = my_str.replace(" ", "|")
new_str = my_str.split("|")
print(f"字符串{my_str}中有{count}个\"it\"")
print(my_str)
print(s2)
print(new_str, type(new_str))
print(f"字符串的长度是{len(my_str)}")
"""
"""
my_str = "万过薪月 员序程马黑来 nohtyp学"
new_str = my_str[::-1]
s1 = new_str.split(" ")
s2 = s1[1]
print(s2)
s3 = s2.replace("来", "")
print(s3)
"""
# 反转list
"""
l1 = []
for i in range(10):
    l1.append(i+1)
l2 = []
for j in range(len(l1)):
    l2.append(l1.pop(-1))
    print(l2[j])
print(l2)
"""
# 集合
"""
summary = set()
n = int(input("请输入集合中有多少元素"))
for i in range(n):
    num = int(input("请输入第%d个元素" % (i+1)))
    summary.add(num)
print(summary)
summary.remove(5)
print(summary)
result = summary.pop()
print(result)
print(summary)
print(len(summary))
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
s3 = s1.union(s2)
print(s3)
print(s1)
print(s2)
s4 = s2.difference(s1)
print(s4)
print(s2)
s2.difference_update(s1)
print(s2)
"""
"""
# 集合练习
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {1, 2, 3, 4, 5}
set3 = {4, 5, 6, 7, 8}
n = int(input("你想要添加几个元素到集合中?"))
for i in range(n):
    num = int(input("请输入第%d个元素" % (i + 1)))
    set1.add(num)
print(f"set1修改后的值是{set1}")
key = int(input("请输入想要删除的元素"))
set1.remove(key)
print(set1)
result = set1.pop()
print(f"从set1中随机取出一个元素值为{result}")
print(set1)
set4 = set1.difference(set2)
print(set4)
print(set1)
print(set2)
set1.difference_update(set2)
print(set2)
print(set1)
"""
'''
import random
random_num = random.randint(1, 11)
print(random_num)
# 数据容器练习
# list
# 创建（初始化）列表
my_list = []
n = int(input("列表中有多少个元素?"))
for i in range(n):
    num = int(input(f"请输入第{i+1}个元素"))
    my_list.append(num)
print("成功初始化", my_list)
# 插入元素
element = int(input("请输入你想要插入的元素"))
length = len(my_list)
place = int(input("请输入你想要插入的位置"))
if place > length:
    print("插入位置不合法")
else:
    my_list.insert(place, element)
    print("成功插入", my_list)
# 查找元素
check = int(input("请输入你想要查找的元素"))
result = my_list.index(check)
print("下标是%d" % result)
# 删除元素
place = int(input("请输入你想要删除的位置"))
length = len(my_list)
if place > length - 1:
    print("删除位置不合法")
else:
    del my_list[place]
    print("删除成功", my_list)
# 翻转链表
my_list.reverse()
print(my_list)
# 指定元素删除
key = int(input("请输入你想要删除的元素"))
if key in my_list:
    my_list.remove(key)
    print(f"成功删除{my_list}")
else:
    print("无法找到该元素")
    print(my_list)
# 统计列表长度
length = len(my_list)
print(f"列表现在的长度是{length}")
# 统计一个元素在列表中出现了几次
element = int(input("请输入你想要统计的元素"))
if element in my_list:
    count = my_list.count(element)
    print(f"{element}在列表中出现了{count}次")
else:
    print("未找到该元素")
    print(my_list)
# 清除列表
my_list.clear()
print("成功清除", my_list)
'''
"""
# 元组练习
# 初始化元组
# t1 = tuple(1, 2, 3, 4, 5, 6, 7)
t2 = (1, 2, 3, 4, 5, 6, 7, 8)
print(t2)
# 遍历
for i in t2:
    print(i)
# 统计某个元素在元组中出现了几次
number = int(input("请输入你想要统计的元素"))
if number in t2:
    count = t2.count(number)
    print(f"{number}在元组中出现了{count}次")
else:
    print("该元素不在元组中")
# 查找元素的下标
element = int(input("请输入你想要查询的元素"))
if element in t2:
    place = t2.index(element)
    print(f"{element}在元组中的下标是{place}")
else:
    print(f"{element}在元组中无法找到")
# 得到元组中的最值
max_number = max(t2)
min_number = min(t2)
print(f"元组中的最大值是{max_number},元组中的最小值是{min_number}")
# 元组切片
t3 = t2[::]  # 全切片
t4 = t2[:5]  # 部分切片
t5 = t2[::2]  # 步长为2的切片
print(t3)
print(t4)
print(t5)
"""

# 字符串练习
# 字符串和数字的转化


# s1 = "123456"
# print(f"s1是{s1},其类型是{type(s1)}")
# n1 = int(s1)
# print(f"n1是{n1},其类型是{type(n1)}")
# # 数字转化字符串
# s2 = str(n1)
# print(f"n1是{n1},其类型是{type(n1)}")
# print(f"s2是{s2},其类型是{type(s2)}")
# print("转化成功")

# # 初始化字符串
# s1 = "   \"apple\"   \"pear\"   \"watermelon\"   "
#
# # 获得字符串长度
# length = len(s1)
# print(f"这个字符串长{length}")
#
# # 遍历字符串
# for i in s1:
#     print(i)
#
# # 查找元素在字符串中的下标
# print(s1)
# element = input("请输入要查找的元素")
# if element in s1:
#     place = s1.index(element)
#     print(f"{element}在s1中的下标是{place}")
# else:
#     print("无法找到该元素")
#
# # 统计元素在字符串中出现了几次
# print(s1)
# element = input("请输入想要统计的元素")
# if element in s1:
#     count = s1.count(element)
#     print(f"{element}在s1中出现了{count}次")
# else:
#     print("未找到该元素")
#
# # 字符串替换
# r_element = input("请输入你要替换的元素")
# re_element = input("请输入你要替换的内容")
# news = s1.replace(r_element, re_element)
# print(f"将{s1}替换为{news}成功")
#
# # 字符串规整
# news1 = s1.strip()
# print(f"将{s1}规整为{news1}成功")
#
# # 字符串切割
# tag = input("请输入你想根据什么来切割?")
# l1 = s1.split(tag)
# print(f"将{s1}按照{tag}切割成{l1}成功")
# print(f"切割后的类型是{type(l1)}")

# 集合练习
# 定义空集合
# set1 = set()
# print(f"set1是一个空集合,其类型是{type(set1)}")
# set2 = {}  # 像这样定义，不能得到一个空集合，只能得到一个空字典
# # 因为字典的定义已经占用了这种定义方法
# print(f"set2这种定义方法只能得到一个空字典,其类型是{type(set2)}")
# set3 = {"apple", "pear", "watermelon"}
# print(f"set3是一个空集合,{set3},其类型是{type(set3)}")

# 水果忍者
#
# # 初始化水果集合
# set1 = set()
# n = int(input("请输入有多少种水果"))
# for i in range(n):
#     fault = input("请输入第%d种水果" % (i + 1))
#     set1.add(fault)
# print(set1)
#
# # 遍历水果
# j = 0
# for i in set1:
#     print(f"这是第{j + 1}种水果,它是{i}")
#     j += 1
#
# # 添加水果
# fault = input("添加一个水果")
# set1.add(fault)
# print(f"添加成功,{set1}")
#
# # 删除水果
# fault = input("请输入你要删除的水果")
# if fault in set1:
#     set1.remove(fault)
#     print(f"删除成功,现在还剩下{set1}")
# else:
#     print("删除失败,集合中没有这个水果")
#
# fault = input("请输入你要删除的水果")
# if fault in set1:
#     set1.discard(fault)
#     print(f"删除成功,现在还剩下{set1}")
# else:
#     print("删除失败,集合中没有这个水果")
#
# # # update  水果
# set2 = {"苹果", "香蕉", "梨"}
# # set1.update(set2)
# # print(f"更新完成,{set1}")
#
# # 集合的运算
# # 交集
# sum_set = set1.union(set2)
# print(sum_set)
# print(set1)
# print(set2)
#
# # 差集
# set3 = set2.difference(set1)  # 返回一个集合,set2中有的并且set1中没有的
# print(set3)
# print(set1)
# print(set2)
#
# # 差集并且更新
# set2.difference_update(set1)
# print(set1)
# print(set2)  # set2中和set1一样的元素被移除了,并且set2被更新

# 字典练习dict

# # 空字典定义
# dict1 = {}  # 定义一个空字典
# print(f"dic1是一个空字典,其内容是{dict1},类型是{type(dict1)}")
# dict2 = dict()  # 定义一个空字典
# print(f"dic2是一个空字典,其内容是{dict2},类型是{type(dict2)}")
# dict3 = {"tt": 18, "jm": 17, "ww": 16}  # 初始化一个字典
# print(dict3)

dict1 = {"apple": 3.14, "pear": 2.5, "banana": 3.6}

# 遍历字典
# 1;
for i in dict1:
    print(f"{i}的价格是{dict1[i]}")
# 2;
keys = dict1.keys()
print(keys)
for i in keys:
    print(f"{i}的价格是{dict1[i]}")

# 通过key查询字典的值
key = input("请输入你想查询什么物品")
if key in dict1:
    print(f"{key}的价格是{dict1[key]}")

# 添加（更新）键值对
key = input("请输入你想要加入什么物品?")
price = input("请输入它的价格")
dict1[key] = price
print(f"操作完成{dict1}")

# 取出商品
key = input("请输入你想要取出什么物品")
if key in dict1:
    result = dict1.pop(key)
    print(f"{key}的价格是{result}")
    print("现在还剩下的商品:", dict1)
else:
    print("没有这个物品")

# 统计字典的长度
length = len(dict1)
print(f"字典现在有{length}个物品")

# 清空字典内容
dict1.clear()
print(f"清空内容成功,其内容变为{dict1}")













