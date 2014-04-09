from scipy import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class point(object):
    x=0.0
    y=0.0
    z=0.0
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

#甯搁噺瀹氫�?
Nc=3            #鑱氱被鏁扮洰
K=3             #棰勬湡鐨勮仛绫绘暟鐩?
MAX_CLUSTER=6   #鏈€澶х殑鑱氱被鏁扮洰
thtN=2          #鑱氱被涓渶灏戠殑鏍锋湰鏁扮�?
thtS=10.0         #鑱氱被涓牱鏈窛绂诲垎甯冪殑鏍囧噯宸紝鏍囧噯宸悜閲忎腑鐨勬渶澶у€间笉瓒呰繃�?
thtC=0.1
step=2          #鐘舵€佹満
MAX_LOOP=100   #鏈€澶ф�?
countLoop=0     #璁板綍姣忔

#---鍑芥暟瀹氫箟鍖?
#姹傛姘忚窛�?
def DistancePoint(x1,y1,z1,x2,y2,z2):
    return ((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**0.5
#涓変釜鏁颁腑姹傛渶澶у�?
def max(x,y,z):
    if(x > y and x>z):
        return [x,1]
    if(y>z):
        return [y,2]
    return [z,3]

pointF=[]       #鏁版�?
pointType=[]    #璁板綍鐐瑰睘浜庣殑绫?
averageD=[]     # 璁板綍姣忎釜鑱氱被鐨勫潎�?
zArray=[]       #鍚勮仛绫讳腑蹇冨�?
lenCluster=[]   #鍚勮仛绫讳腑鐨勬暟鐩?
stdDist=[]      #鍚勮仛绫诲唴鐨勫钩鍧囪窛�?
stdDistArray=[] #姣忚仛绫荤殑鏍囧噯宸悜�?
stdDistMax=[]   #鏍囧噯宸悜閲忎腑鐨勬渶澶у€?
stdDistMaxCor=[]#鏍囧噯宸悜閲忎腑鐨勬渶澶у€肩殑鍧愭爣鍙�?1,y-2,z-3
totalDist=0.0
distMatrix=[]      #Dij全部聚类中心的距�?

#鍒濆鍖栨暟鎹粨鏋?
for i in range(MAX_CLUSTER):
    stdDist+=[0]
    stdDistArray+=[point(0,0,0)]
    lenCluster+=[0]
    zArray+=[point(0,0,0)]
    stdDistMax+=[0.0]
    stdDistMaxCor+=[0]


#璇诲彇鏁版嵁鍒皃ointF
for p in open("iris.txt","r"):
    pointF+=[point(  \
                float(p.split('\n')[0].split('\t')[2]),\
                float(p.split('\n')[0].split('\t')[3]), \
                float(p.split('\n')[0].split('\t')[1]) \
            )]
    pointType+=[-1]

#棰勯€塏c涓仛绫讳腑�?
for i in range(Nc):
    zArray[i]=pointF[i]


for p in pointF:
    print(p.x, p.y,p.z)
print (len(pointF))
#鏁版嵁鐨勬暟�?
dataNUM=len(pointF)

while(countLoop <=  MAX_LOOP):
    if(step==2):
        #灏嗘牱鏈垎缁欐渶杩戠殑鑱氱�
        print("step2-----------------------------------\n")
        for i in range(Nc):
            lenCluster[i]=0
        countLoop += 1
        for i in range(dataNUM):
            mindist=65535
            cluster=-1;
            for c in range(Nc):
                dist = DistancePoint(pointF[i].x, pointF[i].y, pointF[i].z, \
                                      zArray[c].x, zArray[c].y,zArray[c].z )
                if(mindist > dist ) :
                    mindist = dist
                    cluster=c
            #鎵惧埌鏈€杩戠殑鑱氱被锛屽姞杩涘�?
            if (cluster > -1):
                pointType[i]=cluster
                lenCluster[cluster]+=1
        for i in range(Nc):
            print("%d cluster has %d point\n"%(i,lenCluster[i]))

        #璺冲埌绗笁�?
        step=3
    if(step==3):
        print("step3-----------------------------------\n")
        #鍒犻櫎鑱氱被鏁扮洰灏忎簬 thtN鐨勮仛绫?
        for i in range(Nc):
            if(i>=Nc-1):
                continue
            if(lenCluster[i] < thtN):
                #鑱氱被涓殑鏍锋湰鍦ㄤ笅涓€娆″惊鐜殑鏃跺€欙紝鍐嶅垎绫?
                print("del %d cluster\n"%(i))
                for j in range(dataNUM):
                    if(pointType[j] == i):
                        pointType[j]=-1
                del zArray[i]
                zArray+=[point(0,0,0)]
                del lenCluster[i]
                lenCluster+=[0]
                Nc-=1

        step=4
    if(step==4):
        print("step4-----------------------------------\n")
        #淇鍚勮仛绫讳腑蹇冪殑�?
        for i in range(Nc):
            zArray[i].x=0.0
            zArray[i].y=0.0
            zArray[i].z=0.0
        for i in range(dataNUM):
            zArray[pointType[i]].x += pointF[i].x
            zArray[pointType[i]].y += pointF[i].y
            zArray[pointType[i]].z += pointF[i].z
        for i in range(Nc):
            zArray[i].x /=lenCluster[i]
            zArray[i].y /=lenCluster[i]
            zArray[i].z /=lenCluster[i]
            print("%d cluster center is %d,%d,%d"%(i,zArray[i].x, zArray[i].y,zArray[i].z))
        step=5
    if(step==5):
        print("step5-----------------------------------\n")
        #璁＄畻鑱氱被鍐呯殑骞冲潎璺濈�?
        totalDist=0
         #鏁扮粍娓?
        stdDist[:]=bytearray(len(stdDist))
        for i in range(Nc):
            stdDistArray[i].x=0
            stdDistArray[i].y=0
            stdDistArray[i].z=0

        for i in range(dataNUM):
            if(pointType[i] > -1):
                stdDist[pointType[i]] += DistancePoint(pointF[i].x, pointF[i].y, pointF[i].z,\
                                         zArray[pointType[i]].x, zArray[pointType[i]].y,zArray[pointType[i]].z)
                stdDistArray[pointType[i]].x += (pointF[i].x - zArray[pointType[i]].x)**2
                stdDistArray[pointType[i]].y += (pointF[i].y - zArray[pointType[i]].y)**2
                stdDistArray[pointType[i]].z += (pointF[i].z - zArray[pointType[i]].z)**2
        tempDataNum=0;
        for i in range(Nc):
            totalDist+=stdDist[i]
            tempDataNum+=lenCluster[i]

            stdDistArray[i].x /=lenCluster[i]   #鏍囧噯宸悜閲忥紝绗叓姝ヨ璁＄畻鐨?
            stdDistArray[i].x /= (stdDistArray[i].x)**0.5
            stdDistArray[i].y /=lenCluster[i]
            stdDistArray[i].y /= (stdDistArray[i].y)**0.5
            stdDistArray[i].z /=lenCluster[i]
            stdDistArray[i].z /= (stdDistArray[i].z)**0.5
            print(i,Nc)
            print(max(stdDistArray[i].x,stdDistArray[i].y,stdDistArray[i].z))
            [stdDistMax[i],stdDistMaxCor[i]] = max(stdDistArray[i].x,stdDistArray[i].y,stdDistArray[i].z)
            #stdDistMax[i] = max(stdDistArray[i].x,stdDistArray[i].y,stdDistArray[i].z)
            #stdDistMaxCor[i] = max(stdDistArray[i].x,stdDistArray[i].y,stdDistArray[i].z)

            stdDist[i] /= lenCluster[i]
        step=6
        #鍏ㄩ儴鏍锋湰璺濈鍏剁浉搴旂殑鑱氱被涓績鐨勬€诲钩鍧囪窛绂?
        totalDist /= tempDataNum
        step=7
    if(step==7):
        print("step7-----------------------------------\n")
        #鍒ゆ柇鍒嗙被锛屽悎骞朵互鍙婅凯浠ｈ繍�?
        if(countLoop >= MAX_LOOP ):  #杩唬娆℃暟宸插埌锛屽仠姝㈣凯浠?
            step=11
        if(Nc <= K/2):              #鑱氱被鏁扮洰涓嶅埌鏈熸湜鐨勪竴鍗婏紝杩涘叆绗叓姝ュ垎�?
            step=8
        if(countLoop %2 ==0 | Nc >=2*k):    #鑱氱被鏁扮洰澶锛屼互50%鐨勬鐜囦笉缁忚繃鍚堝苟澶勭�?
            step=11
        step=8
    if(step ==8 ):
        #璁＄畻姣忚仛绫讳腑鏍锋湰璺濈鐨勬爣鍑嗗樊鍚戦噺锛屽凡鍦ㄧ浜旀涓�?
        step=9
    if(step ==9):
        #璁＄畻姣忎竴鏍囧噯宸悜閲忎腑鐨勬渶澶у垎閲忥紝宸插湪绗簲涓嶄腑璁＄�?
        step=10
    if(step==10):
        print("step10-----------------------------------\n")
        Garma=0.5
        temp1=point(-1,-1,-1)
        temp2=point(-1,-1,-1)
        for i in range(Nc):
            if(stdDistMax[i] > thtS):
                if( (stdDist[i] > totalDist and lenCluster[i] > 2(thtN+1)) or \
                    (Nc <= K/2)):
                        #鍑嗗鍒嗚
                        if(stdDistMaxCor==1):
                            temp1=zArray[i].x + stdDistArray[i].x*Garma
                            temp1=zArray[i].y
                            temp1=zArray[i].z
                            temp2=zArray[i].x - stdDistArray[i].x*Garma
                            temp2=zArray[i].y
                            temp2=zArray[i].z
                        if(stdDistMaxCor==2):
                            temp1=zArray[i].x
                            temp1=zArray[i].y + stdDistArray[i].y*Garma
                            temp1=zArray[i].z
                            temp2=zArray[i].x
                            temp2=zArray[i].y - stdDistArray[i].y*Garma
                            temp2=zArray[i].z
                        if(stdDistMaxCor==3):
                            temp1=zArray[i].x
                            temp1=zArray[i].y
                            temp1=zArray[i].z + stdDistArray[i].z*Garma
                            temp2=zArray[i].x
                            temp2=zArray[i].y
                            temp2=zArray[i].z - stdDistArray[i].z*Garma
                        zArray[i].x = temp1.x
                        zArray[i].y = temp1.y
                        zArray[i].z = temp1.z
                        zArray[Nc].x = temp2.x
                        zArray[Nc].y = temp2.y
                        zArray[Nc].z = temp2.z
                        Nc+=1
                        i=Nc        #闄愬埗浜嗘瘡涓惊鐜彧鑳藉垎瑁備竴�?
                        step=2
        step=11
    if(step==11):
        #璁＄畻鍏ㄩ儴鑱氱被涓績鐨勮窛绂?
        print("step11-----------------------------------\n")
        #distMatrix=np.dot(zArray,zArray)
        minDist=65535.0
        p1=0
        p2=0
        tempDist=0.0
        for i in range(Nc):
            for j in range(Nc):
                tempDist = DistancePoint(zArray[i].x, zArray[i].y,zArray[i].z, \
                                        zArray[j].x, zArray[j].y,zArray[j].z)
                if(minDist > tempDist):
                    min1 = tempDist
                    p1=i;p2=j
        step=13
        if minDist < thtC :
            #�ϲ���ÿ�κϲ�һ��������С�ĺϲ�
            tempx=(zArray[p1].x * lenCluster[p1] + zArray[p2].x *lenCluster[p2]) / \
                    (lenCluster[p1]+lenCluster[p2])
            tempy=(zArray[p1].y * lenCluster[p1] + zArray[p2].y *lenCluster[p2]) / \
                    (lenCluster[p1]+lenCluster[p2])
            tempz=(zArray[p1].z * lenCluster[p1] + zArray[p2].z *lenCluster[p2]) / \
                    (lenCluster[p1]+lenCluster[p2])
            zArray[p1].x = tempx
            zArray[p1].y = tempy
            zArray[p1].z = tempz
            del zArray[p2]
            zArray+=[point(0,0,0)]
        step=2
        if(countLoop >= MAX_LOOP):
            step = 14
    if step ==14:
        #��ʾ
         print("step14-----------------------------------\n")
         fig = plt.figure()
         ax = fig.add_subplot(111, projection='3d')
         colorA='rgbcykw'
         markerA='o^o^o^o^o'
         for i in range(dataNUM):
             ax.scatter(pointF[i].x,pointF[i].y,pointF[i].z, c=colorA[pointType[i]], marker=markerA[pointType[i]])

         plt.show()
         break










