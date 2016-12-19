#-*-coding:utf-8-*-
#description: 管理层语料项目
#author：FSOL
#Python 3.5.2 64-bit
import os
class MineError(ValueError):
    pass
class EndError(MineError):
    pass
class NoCoError(MineError):
    pass

class afile:
    filename = ''
    fin = open('temp','r',encoding = 'UTF-8')
    fin.close()
    fout = open('temp','w',encoding = 'UTF-8')
    fout.close()
    info = ''
    differ = 20
    scode='董事会报告'
    endcode=''
    def __init__(self,file,d = 20):
        self.filename=file
        self.fin = open('input/'+file,'r',encoding = 'UTF-8')
        self.fout = open('output/'+file,'w',encoding = 'UTF-8')
        self.differ = d
    #判断是否结束
    def well(self):
        if(self.info==''):
            raise EndError()
        else:
            return 1
    #读入下一句
    def readnext(self):
        self.info = self.fin.readline()
        self.info = self.info.replace('\u0020','')
        self.info = self.info.replace('\u3000','')
        return self.well()
    #搜索当前句子中是否有列表中的关键词
    def find(self,word):
        return (len(self.info)<=self.differ and self.info.find(word)!=-1)
    
    #从下一行一直搜索到有目标关键词的行
    def keepfind(self,word):
        self.readnext()
        while not self.find(word):
            self.readnext()
    #对下一行分别搜索两组关键词，前一组返回1，后一组返回2，均无返回0
    def doublefind(self,worda,wordb):
        self.readnext()
        if self.find(worda) :
            return 1
        if self.find(wordb) :
            return 2
        return 0

    #跳过片头
    def skip(self):
        self.differ=300
        self.keepfind('目录')
        self.keepfind(self.scode)
    #搜索结束关键词
    def searchend(self):
        for i in range(10):
            temp = self.doublefind('监事会报告','重要事项')
            if(temp != 0):
                break
        self.differ=20
        if(temp == 1):
            self.endcode='监事会报告'
        elif(temp == 2):
            self.endcode='重要事项'
        elif(temp == 0):
            raise NoCoError()

    #三种处理方式
    def nwork(self):
        print('开始模式：一')
        self.skip()
        self.searchend()
        self.keepfind(self.scode)
        while not self.find(self.endcode):
            self.fout.write(self.info)
            self.readnext()
    def hwork(self):
        print('开始模式：二')
        c = '['
        self.skip()
        self.searchend()
        while(c!=']'):
            self.keepfind(self.scode)
            print(self.info)
            c = input()
        c = '['
        while c!=']':
            while not self.find(self.endcode):
                self.fout.write(self.info)
                self.readnext()
            print(self.info)
            c = input()     
    def shwork(self):
        print('开始模式：三')
        os.system('input\\'+self.filename)
        os.system('output\\'+self.filename)

    #计数
    def count(self):
        stn = 0
        end = 0
        try:
            self.skip()
            self.searchend()
            self.keepfind(self.scode)
            stn = 2
            end = 1
            while 1:
                x = self.doublefind(self.scode,self.endcode)
                if(x==1):
                    stn = stn+1
                elif(x==2):
                    end = end+1
        except NoCoError as e:
            print("Can't find endcode!\n")
            return 3
        except EndError as e:
            if stn == 2 and end == 2:
                return 1
            else:
                print("We have %d stn and %d end\n"%(stn,end))
                if stn >= 2 and end >= 2:
                    return 2
                else:
                    return 3
    #选取方式      
    def solve(self,n):
        self.fin.seek(0)
        try:
            if n==1:
                self.nwork()
            elif n==2:
                self.hwork()
            elif n==3:
                self.shwork()
        except EndError as e:
            c = input("You have reached the end!Still wanna move on?('y' or 'Y')\n")
            if not (c=='y'or c=='Y'):
                self.solve(n)
                
    def start(self):
        self.solve(self.count())
        self.fin.close()
        self.fout.close()
'''
if __name__ == '__main__':
    for i in os.listdir('input/'):
        print(i)
        x = afile(i)
        x.start()'''
        
