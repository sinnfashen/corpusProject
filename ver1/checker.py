#-*-coding:utf-8-*-
#description: 判断处理方法
#author：FSOL
#Python 3.5.2 64-bit

import os
root = os.getcwd()
info = "NaN"
endcode = "NaN"
differ = 20#关键词所在行长度的阈值
print("第二阶段 运行中...")
def errtest():
    #对所有关键词多于两次的文件进行记录
    if stn!=2 or etn != 2:
        if ( stn==2 and etn>2 ) or ( stn>2 and etn==2 ) or(stn>2 and etn>2):
            errf = open(os.path.join(root,"err",errfile),'w',encoding = 'UTF-8')
        else:
            errf = open(os.path.join(root,"errlog",errfile),'w',encoding = 'UTF-8')
        errf.close()
        print('error!\n')
        
def readnext():
    global info
    info = fin.readline()
    info = info.replace('\u0020','')
    info = info.replace('\u3000','')

for filename in os.listdir(os.path.join(root,"input")):
    print(filename)
    if(filename.find("补充")!=-1 or filename.find("更正")!=-1):
        continue
    
    errfile = filename[0:-3]+'err'
    fin = open(os.path.join(root,"input",filename), 'r',encoding = 'UTF-8')
    #统计全文中两关键词出现的次数
    stn = 0
    etn = 0
    
    readnext()
    while (info.find("目录") == -1)and(info!=''):
        readnext()
    while (info.find('董事会报告') == -1)and(info!=''):
        readnext()
        
    if info!='':
        stn+=1
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
        else:
            etn+=1
    
    while ((len(info)>differ or info.find('董事会报告') == -1 ) and (info!='')):
        readnext()
    if(info != ''):
        stn+=1
        readnext()
    while info!='':
        if len(info)<=differ:
            if(info.find('董事会报告') != -1):
                stn+=1
            if(info.find(endcode) != -1):
                etn+=1
        readnext()
        
    errtest()
    fin.close()
