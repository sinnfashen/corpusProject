#-*-coding:utf-8-*-
#description: 总调用文件
#author：FSOL
#Python 3.5.2 64-bit
import os
print("本系统由唐瀚林（FSOL）制作，仅用于厦门大学管理层语料项目。\n使用python版本：Python 3.5.2 64-bit\n联系邮箱：tanghanlincpp@163.com\n\n")
x = input("输入0自动运行全套，输入指定数字运行指定阶段\n")
if(x == 0):
    os.system('python fwork.py')
    os.system('python checker.py')
    os.system('python swork.py')
    os.system('python open.py')
elif(x==1):
    os.system('python fwork.py')
elif(x==2):
    os.system('python checker.py')
elif(x==3):
    os.system('python swork.py')
elif(x==4):
    os.system('python open.py')
else:
    print("指令错误\n")

print("程序结束")
