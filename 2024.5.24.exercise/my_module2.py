# 加上all，假如用*导包，则只能用all这个列表中包含的
__all__ = ["compute"]
def compute(a, b):
    print(a - b)
    return None

def printf1():
    print("我是module2中的函数")



if __name__ == '__main__':
    compute(2, 3)