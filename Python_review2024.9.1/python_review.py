# print(type(11))
# number = 3.1415926
# print(type(number))
# print(type(str(number)))
# print(number)
#
# str = "1.25"
# print(type(str))
# print(str)
# print(type(float(str)))
# print(str)


# number = 1
# print(float(number))
#
# name = 'zhangsan'
# print(type(name))
#
# print(2 ** 4)
# print(9 // 2)
#
# """多行注释"""
#
# string1 = '"这"'
# string2 = "'hello'"
# string3 = "\"hello world\""
# print(string3)

# number1 = 5
# number2 = 8
# string = 'hello world'
# print(number1 + number2)
# print(str(number1))
# print(string + str(number1))

# age = 18
# classroom = 9
# name = 'zhangsan'
#
# print("学生:%s  年龄:%d  班级:%d" % (name, age, classroom))

# number = 3.1415926
# print("%8.4f" % number)

# 快速格式化
# name = "张三"
# age = 18
# class_num = 9
#
# print(f"学生: {name}   年 龄: {age}   班级: {class_num}")

# print("请输入名字")
# name = input()
# print(name)

# input()输入的一切，默认都是str
# number = input("请输入一个数字\n")
# print(type(number))

# def sumNumber(number1, number2) -> int:
#     return number1 + number2
#
# if __name__ == '__main__':
#     print(sumNumber(1, 5))
#     print("-------------------------")
#     array = {1, 2, 3, 4, 5, 6}  # 大括号是集合
#     arrayList = [7, 8, 9, 10, 11]
#     for element in array:
#         print(element)
#     for i in range(len(arrayList)):
#         print(arrayList[i])

# python中列表有索引机制，可以通过索引来访问列表中的元素
# python中的集合和字典都没有索引机制，不可以用索引访问这两个

# 列表
my_list = [1, 2, 3, 4, 5, 6]
# 索引遍历
for i in range(len(my_list)):
    print(my_list[i])

print("---------------------")
# 直接遍历
for element in my_list:
    print(element)

# 元组
my_tuple = (1, 2, 3, 4, 5)
for i in range(len(my_tuple)):
    print(my_tuple[i])
# 元组是不可以修改的
my_tuple[1] = 12





