#-*-coding:utf-8-*-
#description: 人工处理
#author：FSOL
#Python 3.5.2 64-bitimport os
root = os.getcwd()
info = "NaN"
endcode = "NaN"
userinp = 0
differ = 20#关键词所在行长度的阈值
print("第三阶段 运行中...\n")
def readnext():
    global info
    info = fin.readline()
    info = info.replace('\u0020','')
    info = info.replace('\u3000','')

#重复fwork的流程，不过将处理对象限制在err中存在的文件里
print("使用说明：如果打印的句子是你所要的开头/结尾 输入‘]’,否则输入其它\n")

for filename in os.listdir(os.path.join(root,"err")):
    print(filename)
    
    userinp = '['
    fin = open(os.path.join(root,"input",filename[0:-3]+'txt'),'r',encoding = 'UTF-8')
    fout = open(os.path.join(root,"output",filename[0:-3]+'txt'),'w',encoding = 'UTF-8')
    
    readnext()
    while (info.find("目录") == -1)and(info!=''):
        readnext()
    while ((info.find('董事会报告') == -1)and(info!='')):
        readnext()
    
    if info!='':
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
        if(endcode=='NaN'):
            info = ''
            
    #显示查找到带关键词的行，以进行人工判断，用户输入非[意为该行为目标行
    while userinp == '[':
        while ((len(info)>differ or info.find('董事会报告') == -1 ) and (info!='')):
            readnext()
        print(info)
        userinp = input("begin?:")
        if(userinp == '['):
            readnext()
    userinp = '['
    while userinp == '[':
        while ((len(info)>differ or info.find(endcode) == -1 )and(info!='')):
            fout.write(info)
            readnext()
        print(info)
        userinp = input("end?:")
        if(userinp == '['):
            fout.write(info)
            readnext()
    fin.close()
    fout.close()
