# python中的循环

# while循环
# 这是一个简单的while循环，注意，python中没有i++这种自增运算
# while循环的是由while循环的条件控制的，只要条件是True，则循环就会执行
# i: int = 0
# while i != 10:
#     print(i)
#     i = i + 1
# print("______________________________________")
#
# # for循环
# # for循环主要是用于遍历可以迭代的对象，循环次数取决于迭代对象的长度
# # 因为迭代对象不可能无限长，所以说理论上而言，for循环无法实现无限循环
# array: list = [1, 2, 3, 4, 5]
# for i in range(len(array)):
#     print(array[i])
# # range函数可以从0开始，产生参数个数字供for循环轮询
# print("______________________________________")
#
#
# for i in range(10):
#     print(i)
# print("______________________________________")
#
#
# # for循环还可以直接对数据容器进行遍历
# for element in array:
#     print(element)
# print("______________________________________")
#
# # for循环嵌套遍历二维数组
# double_array: list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(double_array)):
#     for j in range(len(double_array[0])):
#         print(double_array[i][j], end=" ")
#     print("\n")


# 函数

# 主函数
# 一切语言都“需要”一个主函数
# python实际上不强制需要主函数，但是主函数可以使得代码逻辑更加清晰，阅读性更强，所以说应该写主函数

# 这是一个最简单的有返回值的函数，添加了函数注解，提高了阅读性
def add(x: int, y: int) -> int:
    return x + y


def compute(x: int, y: int) -> int:
    return x * y


# python中的函数可以有多个返回值
# 返回多个值，其实是返回了一个元组，要用变量接收这个元组
def swap(x: int, y: int) -> tuple:
    return y, x


# 函数作为函数的参数
# 好处：修改代码的时候，只需要修改调用处的参数，而无需修改其他代码
def func(x: int, y: int, add):
    print(add(x, y))


if __name__ == '__main__':
    print("这就是主函数啊")
    number1 = input("请输入第一个数字\n")
    number2 = input("请输入第二个数字\n")
    # print(f"{number1}  {number2}")
    # print(add(int(number1), int(number2)))
    # number1, number2 = swap(int(number1), int(number2))
    # print(f"{number1}  {number2}")

    # 用函数当作函数的参数，只需要在调用处传递新的函数而不做其他修改
    func(int(number1), int(number2), add)
    func(int(number1), int(number2), compute)


