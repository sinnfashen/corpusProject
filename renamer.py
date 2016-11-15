#去除(input子目录下)文件名中的空格
import os
s = os.sep
root = os.getcwd()
directory = os.path.join(root,"input")
for i in os.listdir(directory):
    info=i
    if(info.find(' ') != -1):
        os.rename(directory+s+info,directory+s+info.replace(' ',''))
        
