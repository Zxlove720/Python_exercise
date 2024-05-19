"""
print("C is best")
print(666)
print(13.14)
print("hello world")
"""

# 只是一句注释
"""
这是多行注释
"""

"""
wallet = 50
print("钱包还有", wallet, "元")
print("钱包还有", wallet - 10, "元")
print("钱包还有", wallet - 20, "元")
wallet = wallet - 30
print("钱包还有", wallet - 20, "元")
"""

"""
zxl = "zxl"
print(type(zxl))
print(type("a"))

print(type("love lin"))
print(type(666))
print(type(13.14))
"""

"""
a = 5
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)
"""
'''
z = "z"
x = "x"
l = "l"

print(z, x, l)
phone = 123456
str_phone = str(phone)
print(z + x + l + str_phone)
'''

'''
company_name = input("请输入公司的名字")
stock_price = input("请输入公司今日的股票价格")
stock_code = input("请输入公司的股票代码")
factor = input("请输入增长系数")
days = input("请输入增长了几天")
print(f"公司:{company_name},股票代码是:{stock_code},今日的股价是:{stock_price}")
stock_price = float(stock_price)
stock_code = int(stock_code)
factor = float(factor)
days = int(days)
print("公司:%s,股票代码是:%d,今日的股价是:%.2f,增长%d日后的股价是:%.2f" %
      (company_name, stock_code, stock_price, days, (stock_price * (factor ** days))))
'''
# 信息收集
'''
name = input("请输入姓名")
age = input("请输入年龄")
age = int(age)
gender = input("请输入性别")
ID = input("请输入身份信息")
money = input("请输入你的资产")
money = int(money)
print(f"姓名:{name} 性别:{gender} 年龄:{age} 身份证号:{ID} 资产:{money} ")
print("姓名:%s 性别:%s 年龄:%d 身份证号:%s 资产:%d " % (name, gender, age, ID, money))
'''
'''
flag = True
print(f"结果是{flag},   {type(flag)}")
'''

'''
age = input("请输入年龄")
age = int(age)
if age > 18:
    print("YES")
else:
    print("NO")
'''
'''
name = input("请输入你的名字")
age = int(input("请输入你的年龄"))
if age < 18 | age > 30:
    print("年龄不符合")
else:
    print("年龄符合")
    rank = int(input("请输入你的等级"))
    age = int(input("请输入你的年限"))
    if rank >= 2:
        print("等级符合")
    elif age >= 3:
        print("年限符合")
    else:
        print("等级和年限都不符合")
'''
# 猜数字
'''
import random
rand_number = random.randint(1, 10)
count = 0
flag = True
while count < 5:
    count += 1
    number = int(input("请输入你第%d次猜的数字" % count))
    if number == rand_number:
        print("恭喜你，猜对了")
        print("你一共猜了%d次" % count)
        flag = False
        break
    elif number > rand_number:
        print("猜大了，请再猜一次")
    else:
        print("猜小了，请再猜一次")
if flag:
    print("猜失败了")
'''

# 等差数求和
'''
i = 1
summary = 0
while i <= 100:
    summary += i
    i += 1
print("%d" % summary)
'''

# 统计字符
'''
char = input("请输入字符")
count = 0
for x in char:
    if x == 'a':
        count += 1
print("%d" % count)
'''
'''
for x in range(10):
    print("jizhang")
    for y in range(10):
        print("jizhang")
'''
# 九九乘法表
'''
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%2d " % (j, i, (i*j)), end='')
    print("\n")
'''
'''
money = 10000
count = 0
import random
for i in range(1, 21):
    if money == 0:
        print("工资不够了")
        break
    rank = random.randint(1, 10)
    if rank < 5:
        continue
    else:
        print("成功发工资")
        money -= 1000
'''
# 计算BMI
weight = float(input("输入体重(kg)"))
height = float(input("输入身高(m)"))
BMI = weight / (height ** 2)
print("%.2f" % BMI)
if BMI < 18.5:
    print("偏瘦")
elif BMI >= 18.5 and BMI < 23.9:
    print("正常")
elif BMI >= 23.9 and BMI < 27.9:
    print("超重")
else:
    print("肥胖")





