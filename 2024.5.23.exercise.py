# 数据容器练习

# 列表极其基本操作

# 定义一个列表
# my_list = []  # 空列表
# n = int(input("列表中有几个元素?"))
# for i in range(n):
#     element = int(input("请输入第%d个元素" % (i + 1)))
#     my_list.append(element)
# print(my_list)
#
# # 增加一个元素
# element = int(input("请输入你想要增加的元素"))
# my_list.append(element)
# print(f"增加成功,现在列表中{my_list}")
#
# # 插入一个元素
# element = int(input("请输入你想要插入的元素"))
# place = int(input("请输入你想要插入的位置"))
# if place <= len(my_list):
#     my_list.insert(place, element)
# else:
#     print("插入失败，插入位置不合法")
# print(my_list)
#
# # 删除一个元素
# place = int(input("请输入你想要删除的元素的下标"))
# if place <= len(my_list) - 1:
#     del my_list[place]
# else:
#     print("删除失败，删除位置不合法")
# print(my_list)
#
# # 查找一个元素
# element = int(input("请输入你想要查找的元素"))
# if element in my_list:
#     result = my_list.index(element)
#     print(f"成功找到该元素,其下标是{result}")
# else:
#     print("未能成功找到该元素")
#
# # 修改一个元素
# element = int(input("请输入你想要修改的元素?"))
# if element in my_list:
#     place = my_list.index(element)
#     del my_list[place]
#     element = int(input("请输入你想将其修改为什么元素"))
#     my_list.insert(place,element)
#     print(f"修改成功{my_list}")
# else:
#     print("未能成功找到该元素")
#
# # 统计列表中的元素个数
# length = len(my_list)
# print(f"现在列表中一共有{length}个元素")
#
# # 统计某个元素在列表中出现了几次
# element = int(input("请输入你想要统计的元素"))
# if element in my_list:
#     count = my_list.count(element)
#     print(f"{element}在列表{my_list}中出现了{count}次")
# else:
#     print("列表中未能找到该元素")
#
# # 按值删除元素
# element = int(input("请输入你想要删除的元素值"))
# if element in my_list:
#     my_list.remove(element)
#     print(f"删除成功,列表现在元素还有{my_list}")
# else:
#     print("删除失败,列表中未能找到该元素")
#
# # pop取出元素
# place = int(input("请输入你想要取出第几个元素"))
# if place <= len(my_list) - 1:
#     result = my_list.pop(place - 1)
#     print(f"成功取出下标为{place - 1}的元素{result},现在还剩{my_list}")
# else:
#     print("取出失败,列表中未能找到该元素")
#
# # 排序
# my_list.sort(reverse=False)
# print(my_list)
#
# # 列表后添加列表
# new_list = []
# n = int(input("请输入要添加的列表的元素个数"))
# for i in range(n):
#     num = int(input(f"请输入第{i + 1}个元素"))
#     new_list.append(num)
# my_list.extend(new_list)
# print(f"添加完成{my_list}")
#
# # 求极值
# max_number = max(my_list)
# min_number = min(my_list)
# print(f"列表中的最大值是{max_number},最小值是{min_number}")
#
# # 清空列表内容
# my_list.clear()
# new_list.clear()
# print(my_list)
# print(new_list)

# 元组练习
# 定义元组
# t1 = ()  # 简化的定义方法
# t2 = tuple()  # 相对规范的定义方法
# 元组不能修改，所以说像上面两个元组相当于已经没什么用了

#
# # 定义元组并且初始化
# t1 = ("apple", "pear", "watermelon", "milk")
#
# # 查找元素
# element = input("请输入你想要查找的元素")
# if element in t1:
#     place = t1.index("apple")
#     print(f"成功找到,其下标为{place}")
# else:
#     print("无法找到%s" % element)
#
# # 统计一个元素在元组中出现了几次
# element = input("请输入要统计的元素")
# if element in t1:
#     count = t1.count(element)
#     print(f"{element}在元组t1中出现了{count}次")
# else:
#     print("无法找到该元素")
#
# # 求极值和元素个数
# count = len(t1)
# print(f"元组中元素个数是{count}")
# max_number = max(t1)
# min_number = min(t1)
# print(f"元组中的最大值是{max_number},元组中的最小值是{min_number}")
#

# 字符串练习
# 定义一个字符串
#
# my_str = "   apple   pear   watermelon   orange   "
#
# # 查找一个元素的下标
# element = input("请输入想要查找的元素")
# if element in my_str:
#     result = my_str.index(element)
#     print(f"{element}的下标是{result}")
# else:
#     print(f"{element}在{my_str}中没有出现")
#
# # 统计一个字符出现了几次
# element = input("请输入要统计的字符")
# if element in my_str:
#     count = my_str.count(element)
#     print(f"{element}在{my_str}出现了{count}次")
# else:
#     print(f"{element}在{my_str}中没有出现")
#
# # 找到极值元素
# max_element = max(my_str)
# min_element = min(my_str)
# print(f"{my_str}中最大的元素是{max_element},最小的元素是{min_element}")
#
# # 字符串替代
# element = input("请输入你想要替代什么元素")
# if element in my_str:
#     new_element = input("请输入你想要用什么来替代它")
#     new_str = my_str.replace(element, new_element)
#     print(f"用{new_element}替代{my_str}中的{element}成功")
#     print(new_str)
# else:
#     print(f"{my_str}中没有{element}")
#
# # 字符串切割
# element = input("请输入你想用什么元素进行切割?")
# if element in my_str:
#     s1 = my_str.split(element)
#     print("切割成功", s1)
# else:
#     print("用来切割的元素不在串内")
#

# 函数练习
# 函数返回多个值
"""
def compute(a, b):
    return a + b, a - b, a * b, a / b

a = int(input("a"))
b = int(input("b"))
x1, x2, x3, x4 = compute(a, b)
print("a+b=", x1)
print("a-b=", x2)
print("a*b=", x3)
print("a/b=", x4)
"""
# 函数的位置参数
# 按照位置参数和形参一一对应
"""
def information(name, age, gender):
    print(f"姓名:{name},年龄{age},性别{gender}")
    return None
name = input("name")
age = input("age")
gender = input("gender")
information(name, age, gender)
"""

# def information(name, age, gender):
#     print(f"name:{name} age:{age} gender{gender}")
#     return None
#
# name = input("name")
# age = input("age")
# gender = input("gender")
# information(name=name, age=age, gender=gender)
# information(age=age, gender=gender, name=name)
# information("卷毛", gender=gender, age=age)

# def information(name, age="jiejie", gender="塑料袋"):
#     print(f"name:{name} age:{age} gender{gender}")
#     return None
#
# name = input("nmae")
# age = input("age")
# gender = input("gender")
# information(name)


# def information(*args):
#     print(args)
# name = input("name")
# age = input("age")
# gender = input("gender")
# tall = input("tall")
# weight = input("weight")
# information(name, age, gender, tall, weight)


def information(**kwargs):
    print(kwargs)
information(apple=10, pear=20, lemon=30)



