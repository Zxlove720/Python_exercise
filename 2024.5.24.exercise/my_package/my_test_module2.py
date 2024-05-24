def my_print1():
    print("我是包中的module2中的函数1")
    return None

def my_print2():
    print("我是包中的module2中的函数2")
    return None

if __name__ == '__main__':
    my_print1()
    my_print2()