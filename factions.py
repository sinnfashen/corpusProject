class MineError(ValueError):
    pass
class EndError(MineError):
    pass
class NoCoError(MineError):
    pass

class afile:
    fin = 0
    fout = 0
    differ = 20
    info = 'NaN'
    endcode ='NaN'
    scode='董事会报告'
    def __init__(self,indir,outdir,d = 20):
        global fin,fout,differ
        fin = open(indir,'r',encoding = 'UTF-8')
        fout = open(outdif,'w',encoding = 'UTF-8')
        differ = d
        
    def well(self):
        if(info==''):
            raise EndError()
        else:
            return 1
    
    def readnext(self):
        global info
        info = fin.readline()
        info = info.replace('\u0020','')
        info = info.replace('\u3000','')
        return well

    def find(self,word):
        return (len(info)<=differ and info.find(word) != -1)
    
    def keepfind(self,word):
        readnext()
        while !find(word):
            readnext()

    def doublefind(self,worda,wordb):
        readnext()
        if find(worda) :
            return worda
        if find(wordb) :
            return wordb
        return 'NaN'
    
    def skip(self):
        keepfind('目录')
        keepfind(sword)

    def searchend(self):
        global endcode
        for i in range(10):
            endcode = doublefind('监事会报告','重要事项')
            if(endcode != 'NaN'):
                break
        if(endcode == 'NaN'):
            raise NoCoError()
    def nwork():
        fin.seek(0)
        skip()
        searchend()
        keepfind(scode)
        while !find(endcode):
            fout.write(info)
            readnext()

    def hwork()
        c = ']'
        fin.seek(0)
        skip()
        searchend()
        while(c==']'):
            keepfind(scode)
            print(info)
            input(c)
        c = ']'
        while c==']':
            while !find(endcode):
                fout.write(info)
                readnext()
            input(c)
            
    def count(self):
        fin.seek(0)
        stn = 0,end = 0
        try:
            skip()
            searchend()
            keepfind(scode)
            stn = 2,end = 1
            while 1:
                x = doublefind(sword,endcode)
                if(x==sword)
                    stn = stn+1
                elif(x==endcode)
                    end = end+1
        except NoCoError as e:
            print("Can't find endcode!\n")
            return 3
        except EndError as e:
            if stn == 2 and end == 2:
                return 1
            else:
                print("We have %d stn and %d end\n")
                if stn >= 2 and end >= 2:
                    return 2
                else:
                    return 3
    def solve(self,n):
        try:
            if n==1:
                nwork()
            elif n==2:
                hwork()
            elif n==3:
                shwork()
        except EndError as e:
            c = input("You have reached the end!Still wanna move on?('y' or 'Y')\n")
            if !(c=='y'or c=='Y'):
                solve(n)
    def main():
        solve(count())
