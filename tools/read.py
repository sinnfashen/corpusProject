#-*-coding:utf-8-*-
#description: 用来输出并测试
#author：FSOL
#Python 3.5.2 64-bit
f = open("600193_创兴资源2014年年度报告.pdf.txt", 'r',encoding = 'UTF-8')
for i in range(1, 300 + 1):
    print(i)
    print("     "+f.readline())
