class point(object):
    x=0.0
    y=0.0
    z=0.0
pointF=[]
pointType=[]#璁板綍鐐瑰睘浜庣殑绫?
AverageD=[]# 璁板綍姣忎釜鑱氱被鐨勫潎鍊?
ZArray=[]


StdDiff=[]   # 璁板綍鑱氱被鏍锋湰涓績鏍囧噯宸€?
Std=[]       #鏍囧噯鑱氱被涓績
Sum=[]       #姹傚拰涓存椂
N=[]          #璁板綍姣忎釜鑱氱被涔﹂潰

StdDistance=[] #鑱氱被涓績涔嬮棿璺濈
StdDisMax=[]
StdDisMaxCor=[]

MaxDiff=1        #鏍囧噯宸垽瀹氬尯闂?
MinDistance=2    #涓嶅悓鑱氱被涓績鏈€灏忚窛绂?
MaxNumStd=4      #鏈€澶х殑鑱氱被涓績鏁扮洰
TotalNum=10       #鐐规暟

SAArray=[[]]
ZDistance=[]
ZDistanceR=[]
ZDistanceC=[]
StdTime=10
Nc=4
step=2             #璁板綍姝ラ鍙婂綋鍓嶇姸鎬?
CountTime=0
#---------------------------------鍒濆鍖?
for i in range(TotalNum):
    pointF+=[point()]
    pointType+=[0]
    StdDiff+=[point()]
    ZDistance+=[0]
    ZDistanceR+=[0]
    ZDistanceC+=[0]
for i in range(MaxNumStd):
    AverageD+=[0]
    Std+=[point()]
    Sum+=[point()]
    ZArray+=[point()]
    N+=[0]
for i in range(MaxNumStd):
    StdDistance+=[point()]
    StdDisMax+=[0]
    StdDisMaxCor+=[0]
for i in range(TotalNum):
    SAArray+=[[]]
    for j in range(TotalNum):
        SAArray[i]+=[point()]

[pointF[0].x,pointF[0].y]=[0.0,0.0]
[pointF[1].x,pointF[1].y]=[3.0,8.0]
[pointF[2].x,pointF[2].y]=[2.0,2.0]
[pointF[3].x,pointF[3].y]=[1.0,1.0]
[pointF[4].x,pointF[4].y]=[5.0,3.0]
[pointF[5].x,pointF[5].y]=[4.0,8.0]
[pointF[6].x,pointF[6].y]=[6.0,3.0]
[pointF[7].x,pointF[7].y]=[5.0,4.0]
[pointF[8].x,pointF[8].y]=[6.0,4.0]
[pointF[9].x,pointF[9].y]=[7.0,5.0]
[ZArray[0].x,ZArray[0].y]=[0,0]
[ZArray[1].x,ZArray[1].y]=[3,8]
[ZArray[2].x,ZArray[2].y]=[2,2]
[ZArray[3].x,ZArray[3].y]=[1,1]
#----------------------------------鍑芥暟瀹氫箟鍖?
def DistancePoint(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
def DistancePointF(a,b):
    return ((a.x-b.x)**2+(a.y-b.y)**2)**0.5
def ComputeNumStd(TypeList):
    temp=pointType[7]
    for i in range(6):
        if temp<pointType[i]:
            temp=pointType[i]
    return temp+1
while(CountTime<=StdTime):
    if step==2:
        for i in range(Nc):
            N[i]=0
        print ('杩欐槸绗?d娆″綊绫?%CountTime)
        CountTime=CountTime+1
        stdtemp=0
        for i in range(TotalNum):
            dis=65535
            for j in range(Nc):
                ftemp=DistancePointF(pointF[i],ZArray[j])
                if ftemp<dis:
                    stdtemp=j
                    dis=ftemp
            SAArray[stdtemp][N[stdtemp]].x=pointF[i].x
            SAArray[stdtemp][N[stdtemp]].y=pointF[i].y
            N[stdtemp]=N[stdtemp]+1
        for i in range(Nc):
            print ("绗?d涓仛绫讳腑蹇冩槸:(%d,%d)鎷ユ湁%d涓厓绱?  "%(i,ZArray[i].x,ZArray[i].y,N[i]))
            print ("鍖呭惈鐨勫厓绱犳湁锛?)
            for j in range(N[i]):
                print ("(%d,%d)"%(SAArray[i][j].x,SAArray[i][j].y))
        step=3   #璺宠浆鍒扮涓夋
        #break
    if step==3:
        print("绗?d姝ワ紝鍒ゆ柇鏄惁鍙互鍘绘帀涓€浜?%step)
        for i in range(Nc):
            if N[i]<1: #1涔熷彲浠ヤ负鍏朵粬褰㈠弬
                #鍙栨秷杩欎釜鏍锋湰瀛愰泦
                for j in range(TotalNum):
                    if pointType[j]==i:
                        pointType[j]=-1
                tr=i
                while(tr<Nc-1):
                    for m in range(N[tr+1]):
                        SAArray[tr][m].x=SAArray[tr+1][m].x
                        SAArray[tr][m].y=SAArray[tr+1][m].y
                    tr=tr+1
                tr=i
                while(tr<Nc-1):
                    N[tr]=N[tr+1]
                    tr=tr+1
                Nc=Nc-1
        step=4
        for i in range(Nc):
            print ("绗?d涓仛绫讳腑蹇冩槸:(%d,%d)   "%(i,ZArray[i].x,ZArray[i].y))
            print ("鍖呭惈鐨勫厓绱犳湁锛?)
            for j in range(N[i]):
                print ("(%d,%d)"%(SAArray[i][j].x,SAArray[i][j].y))
    #break
    if step==4:
        print("绗?d姝ワ紝淇鍚勪釜鑱氱被涓績"%step)
        for i in range(Nc):
            temx=0
            temy=0
            for j in range(N[i]):
                temx+=SAArray[i][j].x
                temy+=SAArray[i][j].y
            ZArray[i].x=temx/N[i]
            ZArray[i].y=temy/N[i]
            print (N[i])
            print ("淇鍚庤仛绫讳腑蹇?d涓?%f锛?f)"%(i,ZArray[i].x,ZArray[i].y))
        step=5
    if step==5:
        print("绗?d姝ワ紝璁＄畻鍚勮仛绫诲煙涓鏍锋湰涓庤仛绫讳腑蹇冪殑骞冲潎璺濈"%step)
        TempAverage=0
        for i in range(Nc):
            for j in range(N[i]):
                TempAverage+=DistancePointF(SAArray[i][j],ZArray[i])
            AverageD[i]=TempAverage/N[i]
            print ("鑱氱被%d鐨勫钩鍧囪窛绂讳负%3f"%(i,AverageD[i]))
            TempAverage=0
        step=6
        #break
    if step==6:
        print ("绗?d姝ワ紝璁＄畻鍏ㄩ儴妯″紡鏍锋湰瀵瑰簲鑱氱被涓績鐨勬€诲钩鍧囪窛绂?%step)
        DAv=0
        for i in range(Nc):
            DAv+=N[i]*AverageD[i]
        DAv/=TotalNum
        print ("鎬诲钩鍧囪窛绂讳负%f"%DAv)
        #break
        step=7
    if step==7:
        print ("绗?d姝ワ紝鍒ゆ柇杞Щ"%step)
        if CountTime>StdTime:
            step=14
            print("杩唬娆℃暟宸茬粡杈惧埌%d娆¤浆绉诲埌绗?d姝?%(StdTime,step))
        elif Nc<=MaxNumStd:
            step=8
            print("杞Щ鍒扮%d姝ワ紝灏嗗凡鏈夌殑鑱氱被鍒嗚"%step)
        elif CountTime%2==0|Nc>2*MaxNumStd:
            step=11
            print("杩唬娆℃暟涓哄伓娆¤浆绉诲埌绗?d姝?%step)
    if step==8:
        print("绗?d姝ワ紝璁＄畻鍚勮仛绫讳腑鏍锋湰璺濈鏍囧噯宸?%step)
        for i in range(Nc):
            temx=0
            temy=0
            for j in range(N[i]):
                temx+=(SAArray[i][j].x-ZArray[i].x)**2
                temy+=(SAArray[i][j].y-ZArray[i].y)**2
            StdDistance[i].x=(temx/N[i])**0.5
            StdDistance[i].y=(temy/N[i])**0.5
            temx=0.0
            temy=0.0
            print( "鑱氱被%d鐨勬爣鍑嗗樊涓猴紙%f锛?f锛?%(i,StdDistance[i].x,StdDistance[i].y))
        step=9
    if step==9:
        print("绗?d姝ワ紝姹傛瘡涓爣鍑嗗樊鍚戦噺涓殑鏈€澶у垎閲?%step)
        for i in range(Nc):
            if StdDistance[i].x>StdDistance[i].y:
                StdDisMax[i]=StdDistance[i].x
                StdDisMaxCor[i]=1
            else:
                StdDisMax[i]=StdDistance[i].y
                StdDisMaxCor[i]=0
            print("鑱氱被%d涓殑鏍囧噯宸渶澶у垎閲忔槸%d涓?f"%(i,StdDisMaxCor[i],StdDisMax[i]))
        step=10
    if step==10:
        print("绗?d姝ワ紝鍒嗚鍒ゆ柇鍜岃绠?%step)
        temp1=point()
        temp2=point()
        Garma=0.5
        for i in range(Nc):
            if StdDisMax[i]>MaxDiff:
                if((AverageD[i]>DAv)&(N[i]>2*(Nc+1)))|Nc<=MaxNumStd/2:
                    if StdDisMaxCor[i]==0:
                        temp1.x=ZArray[i].x+StdDisMax[i]*Garma
                        temp1.y=ZArray[i].y
                        temp2.x=ZArray[i].x-StdDisMax[i]*Garma
                        temp2.y=ZArray[i].y
                    elif StdDisMaxCor[i]==1:
                        temp1.y=ZArray[i].y+StdDisMax[i]*Garma
                        temp1.x=ZArray[i].x
                        temp2.y=ZArray[i].y-StdDisMax[i]*Garma
                        temp2.x=ZArray[i].x
                    ZArray[i].x=temp1.x
                    ZArray[i].y=temp1.y
                    ZArray[Nc].x=temp2.x
                    ZArray[Nc].y=temp2.y
                    print("鑱氱被%d琚垎瑁備负鑱氱被%d鍜岃仛绫?d"%(i,i,Nc))
                    print("鍒嗚鍚庣殑涓績鍒嗗埆涓猴紙%f,%f锛夊拰锛?f,%f锛?%(temp1.x,temp1.y,temp2.x,temp2.y))
                    Nc=Nc+1
                    step=2
                    i=Nc
        step=11
    if step==11:
        print("绗?d姝ワ紝璁＄畻鍏ㄩ儴鑱氱被涓績鐨勮窛绂?%step)
        rank=0
        for i in range(Nc-1):
            j=i+1
            while(j<Nc):
                ZDistance[rank]=DistancePointF(ZArray[i],ZArray[j])
                ZDistanceR[rank]=j
                ZDistanceC[rank]=i
                print("鑱氱被%d涓庤仛绫?d涔嬮棿鐨勮窛绂讳负%f"%(i,j,ZDistance[rank]))
                rank+=1
                j=j+1
        step=12
        #break
    if step==12:
        print("绗?d姝ワ紝鎵惧嚭绫婚棿璺濈鏈€灏忕殑,鍙€冭檻涓€娆″彧鍚堝苟涓€瀵硅仛绫讳腑蹇冪殑鎯呭喌"%step)
        ZDistanceT=ZDistance[0]
        ZDistanceCT=ZDistanceC[0]
        ZDistanceRT=ZDistanceR[0]
        for i in range(rank):
            if ZDistance[i]<ZDistanceT:
                ZDistanceT=ZDistance[i]
                ZDistanceCT=ZDistanceC[i]
                ZDistanceRT=ZDistanceR[i]
        print ("鏈€灏忕殑鑱氱被璺濈涓鸿仛绫?d鍜?d涔嬮棿鐨勮窛绂讳负%f"%(ZDistanceCT,ZDistanceRT,ZDistanceT))
        step=13
        #break
    if step==13:
        print("绗?d姝ワ紝鍚堝苟鑱氱被"%step)
        if(ZDistanceT<MinDistance):
            ZArrayT=point()
            print("鍙互杩涜鍚堝苟鑱氱被,鍚堝苟鑱氱被鑱氱被%d鍜?d鐢熸垚鏂拌仛绫?d"%(ZDistanceCT,ZDistanceRT,ZDistanceCT))
            ZArrayT.x=(N[ZDistanceCT]*ZArray[ZDistanceCT].x+N[ZDistanceRT]*ZArray[ZDistanceRT].x)/(N[ZDistanceCT]+N[ZDistanceRT])
            ZArrayT.y=(N[ZDistanceCT]*ZArray[ZDistanceCT].y+N[ZDistanceRT]*ZArray[ZDistanceRT].y)/(N[ZDistanceCT]+N[ZDistanceRT])
            print ("鑱氱被涓績锛?f,%f锛夎仛绫讳腑蹇冿紙%f锛?f锛夊悎骞跺緱鍑虹殑鏂扮殑鑱氱被涓績涓猴紙%f,%f锛?%(ZArray[ZDistanceCT].x,ZArray[ZDistanceCT].y,ZArray[ZDistanceRT].x,ZArray[ZDistanceRT].y,ZArrayT.x,ZArrayT.y))
            ZArray[ZDistanceCT].x=ZArrayT.x
            ZArray[ZDistanceCT].y=ZArrayT.y
            i=ZDistanceCT
            while(i<Nc-1):
                ZArray[i].x=ZArray[i+1].x
                ZArray[i].y=ZArray[i+1].y
                i=i+1
            i=ZDistanceCT
            while(i<Nc-1):
                N[i]=N[i+1]
                i+=1
            Nc=Nc-1
        step=14
        #break
    if step==14:
        print("绗?d姝ワ紝鏈€鍚庝竴姝ユ樉绀虹粨鏋?%step)
        if CountTime>StdTime:
            print("ISODATA绠楁硶瀹屾瘯涓€鍏卞垎涓?d绫?%Nc)
            for i in range(Nc):
                print ("绗?d涓仛绫讳腑蹇冩槸:(%f,%f)鎷ユ湁%d涓厓绱?  "%(i,ZArray[i].x,ZArray[i].y,N[i]))
                print ("鍖呭惈鐨勫厓绱犳湁锛?)
                for j in range(N[i]):
                    print ("(%f,%f)"%(SAArray[i][j].x,SAArray[i][j].y))
            break
        else:
            step=2



