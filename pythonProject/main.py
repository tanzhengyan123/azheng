#print("hello mimi")

#print("漠莫")

name ="漠漠"
age = 23
height=1.68
weight=55.5

print("我的名字是" + name )

#print("我的年龄是" age)
#%d 只替换整数 %s 替换字符串 %f替换小数

print("我的名字是 %s" % name)
print("我的年龄是 %d" % age)
print("我的身高是 %s" % height)
print("我的体重是 %f" % weight)
print("我的体重是 %.2f" % weight)

#print("我的名字是 %s,我的年龄是 %d,我的身高是 %s,我的体重是 %.2f"%(name,age ,height,weight))

print("我的名字是 %s,\n我的年龄是 %d,\n我的身高是 %s,\n我的体重是 %.2f"%(name,age ,height,weight))

'''
name = "漠漠"
num1 = 98

age = input("请输入您的名字：")

age = int(age)

'''

'''
if age >20:
    print("可以去看电影吗")
else:
    print("回家睡觉吧")
'''


'''
username = input("请输入您的用户名：")
passwdel = input("请输入您的密码：")

if username == "漠漠" and passwdel == "123456":
    print("登录成功")
else:
    print("用户名或者密码错误！")
'''

#or 或者
'''
gao = input("高吗？请输入 Y/N:")
shuai = input("帅吗？请输入 Y/N:")
fu = input("富吗？请输入 Y/N:")
if gao == "Y" and shuai == "Y"and fu == "Y":
    print("今晚有空")
else :
    print("洗澡去了")
'''
#score = input("请输入你的分数：")
#if score >95 and score <=100:
#else: score > 88 and score <=95
    #print("良好")
num1 = int(input("请输入一个数字："))
num2 = int(input("请输入二个数字："))
num3 = int(input("请输入三个数字："))
minnum = num1
if num2 < minnum:
    minnum = num2
if num2 < minnum2:
    minnum = num3
    print(minnum)

#a = 10   b = 20
#a =20    b =10

