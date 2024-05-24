# python文件操作
# f = open("打字版.txt", "a", encoding="UTF-8")
# writer = input("请输入你想要写入到文件的内容")
# f.write(writer)
# f.flush()
# f.close()
# f = open("打字版.txt", "r", encoding="UTF-8")
# i = 1
# for line in f:
#     print(f"第{i}行的内容是{line}")
#     i += 1
# f.close()
#
# with open("打字版.txt", "r", encoding="UTF-8") as f:
#     i = 0
#     for line in f:
#         print(f"第{i}行的内容是{line}")
#         i += 1

#
# f = open("打字版.txt", "r", encoding="UTF-8")
# new_file = open("bill.txt.bak", "w", encoding="UTF-8")
# for line in f:
#     file_line = line.strip()
#     if (file_line.split(",")[4]) == "测试":
#         continue
#     else:
#         new_file.write(file_line)
#         new_file.write("\n")
# f.close()
# new_file.close()

# 异常捕获
#
# try:
#     f = open("zxl.txt", "r", encoding="UTF-8")
# except Exception as e:
#     print(e)
#     f = open("zxl.txt", "w", encoding="UTF-8")
#     f.write("zxl 520")
#     f.close()
#     f = open("zxl.txt", "r", encoding="UTF-8")
# else:
#     print("No Error")
# finally:
#     print(f.read())
#     f.close()

#
# # 异常的传递性
# def func1():
#     return 1/0
# def func2():
#     result = func1()
#     return None
# def func3():
#     func2()
#     return None
#
# try:
#     func3()
# except Exception as error:
#     print(error)
# else:
#     print("No Error")
# finally:
#     print("end")


# 文件操作
# 读文件
f = open("打字版.txt", "r", encoding="UTF-8")
i = 1
f.close()
# 按行读 1
# for line in f:
#     print(f"第{i}行的文件内容是{line}")
#     i += 1
# f.close()
# 按行读 2
# print(f.readlines())
# 按行读 3
# n = int(input("请输入你想读几行?"))
# for i in range(n):
#     print(f.readline())

# 按字节读
#
# n = int(input("请输入你想读几个字节?"))
# for i in range(n):
#     print(f.read(n))
# f.close()
#
# # 写文件
# f = open("wzb.txt", "w", encoding="UTF-8")
# n = int(input("请问你要写入文件的内容有几行?"))
# j = 1
# for i in range(n):
#     files = input(f"请输入你想要写入文件的第{j}行内容")
#     f.write(files)
#     f.write("\n")
#     j += 1
# f.flush()
# f.close()

# 备份文件
# f = open("打字版.txt", "r", encoding="UTF-8")
# new_file = open("bills.txt", "w", encoding="UTF-8")
# for line in f:
#     files = line.strip()  # 先规整字符串
#     if files.split(",")[4] == "测试":  # 再通过","将其分为5个列表中的元素，然后进行对照
#         continue
#     else:
#         new_file.write(line)
#         new_file.write("\n")
# new_file.flush()
# f.close()
# new_file.close()

#
# f = open("打字版.txt", "r", encoding="UTF-8")
# new_file = open("bills.txt", "w", encoding="UTF-8")
# for line in f:
#     files = line.strip()
#     if "测试" in files:
#         continue
#     else:
#         new_file.write(line)
#         new_file.write("\n")
# new_file.flush()
# f.close()
# new_file.close()


# 错误检测
# def func1():
#     return 1 / 0
# try:
#     result = func1()
# except Exception as e:
#     print(e)
# else:
#     print("No Error")

# from time import sleep
# # 倒计时
# j = 5
# for i in range(1, 6):
#     print(j)
#     j -= 1
#     sleep(1)

# from time import *
# print("z")
# sleep(2)
# print("720")
#
# import time as t
# print("z")
# t.sleep(2)
# print("720")

# 自己创造模块
#
# import my_module1
# my_module1.sum_number(1, 2)
#
#
# from my_module1 import sum_number
# sum_number(5, 6)
#
# import my_module1
# my_module1.sum_number(1, 5)
# from my_module2 import *
# compute(2, 3)

#
# import my_package.my_test_module1
# import my_package.my_test_module2
# my_package.my_test_module1.compute2(1, 1)
# my_package.my_test_module2.my_print1()


from my_package import *
my_test_module1.compute1(4, 5)










