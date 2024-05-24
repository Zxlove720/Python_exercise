def sum_number(a, b):
    print(a + b)

def printf():
    print("我正在被调用!")

# 在自己测试模块中内容的时候，只要包含就直接调用
# printf()
# 改用main可以解决这个问题
if __name__ == '__main__':
    printf()
