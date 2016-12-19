#-*-coding:utf-8-*-
#description: 打开文件
#author：FSOL
#Python 3.5.2 64-bit
import os
s = os.sep
root = os.getcwd()
print("第四阶段 运行中...\n")
print("使用说明：\n  本程序会自动先后打开原文件并自动在\output文件夹下新建同名的txt。\n用户需要在第一个打开的txt里把内容复制下来后关闭窗口，才会打开目标文件\n提示是否创建是选择“是”\n")
for filename in os.listdir(os.path.join(root,"errlog")):
    os.system('notepad input\\'+filename[0:-3]+'txt')
    os.system('notepad output\\'+filename[0:-3]+'txt')
    input("任意键继续(推荐回车)")
