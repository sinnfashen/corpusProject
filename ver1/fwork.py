#-*-coding:utf-8-*-
#description: 机器处理
#author：FSOL
#Python 3.5.2 64-bit

import os
s = os.sep
root = os.getcwd()
info = "NaN"
endcode = "NaN"
differ = 20#关键词所在行长度的阈值

print("第一阶段 正在运行中...\n\n")
#读入时去空格
def readnext():
    global info
    info = fin.readline()
    info = info.replace('\u0020','')
    info = info.replace('\u3000','')
    
#对所有middle文件夹下的文件，即转换后的txt
for filename in os.listdir(os.path.join(root,"input")):
    #print(filename)
    if(filename.find("补充")!=-1 or filename.find("更正")!=-1):
        continue
    
    #处理文件的名字并打开
    fin = open(os.path.join(root,"input",filename), 'r',encoding = 'UTF-8')
    fout = open(os.path.join(root,"output",filename),'w',encoding = 'UTF-8')

    #寻找第一个“董事会报告”
    readnext()
    while (info.find("目录") == -1)and(info!=''):
        readnext()
    while (info.find('董事会报告') == -1)and(info!=''):
        readnext()
        
    if info!='':
        #判断董事会报告的下一章节是什么
        readnext()
        count = 0
        while info != '' and count < 10:
            if info.find("监事会报告")!=-1 :
                endcode="监事会报告"
                break
            else:
                if info.find("重要事项")!=-1 :
                    endcode="重要事项"
                    break
            readnext()
            count+=1
        if(endcode=="NaN"):
            info = ''
            
    #寻找第二个董事会报告并输出直到下一章节的关键词出现
    while ((len(info)>differ or info.find('董事会报告') == -1 ) and (info!='')):
        readnext()
    while ((len(info)>differ or info.find(endcode) == -1 ) and (info!='')):
        fout.write(info)
        readnext()
    
    fin.close()
    fout.close()
