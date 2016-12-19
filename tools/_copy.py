#-*-coding:utf-8-*-
#description: 复制小工具
#author：FSOL
#Python 3.5.2 64-bit
import os.path
import shutil
direction = os.getcwd()
for files in os.listdir(os.path.join(direction,'errlog')):
    print(files)
    shutil.copy(os.path.join(direction,'middle',files[0:-3]+'txt'),os.path.join(direction,'copy',files[0:-3]+'txt'))
