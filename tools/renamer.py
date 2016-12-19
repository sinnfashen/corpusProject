#-*-coding:utf-8-*-
#description: 去除(input子目录下)文件名中的空格
#author：FSOL
#Python 3.5.2 64-bit
import os
s = os.sep
root = os.getcwd()
directory = os.path.join(root,"input")
for i in os.listdir(directory):
    info=i
    if(info.find(' ') != -1):
        os.rename(directory+s+info,directory+s+info.replace(' ',''))
        
