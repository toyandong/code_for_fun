#-------------------------------------------------------------------------------
# Name:        k均值算法
# Purpose:
#
# Author:      yandong
#
# Created:     30/10/2013
# Copyright:   (c) yandong 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#import pylab as pl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#num of cent2er
K=3
#read date
points = [ \
            [float(eachpoint.split('\n')[0].split('\t')[1]), \
             float(eachpoint.split('\n')[0].split('\t')[2]), \
             float(eachpoint.split('\n')[0].split('\t')[3]), \
             float(eachpoint.split('\n')[0].split('\t')[4]), \
            ] for eachpoint in open("iris.txt","r")]
print ("date size :"+ str(len(points)))
#
currentCenter1 = points[0]; currentCenter2 =points[50]; currentCenter3 =points[100]
# 记录每次迭代后每个簇的质心的更新轨迹
center1 = [currentCenter1]; center2 = [currentCenter2]; center3 = [currentCenter3]
group1 = []; group2 = []; group3 = []
distance1=0;distance2=0;distance3=0
for runtime in range(1000):
    group1 = []; group2 = []; group3 = []
    for eachpoint in points:
        # 计算每个点到三个质心的距离
        distance1 = pow(abs(eachpoint[3]-currentCenter1[3]),2) + pow(abs(eachpoint[1]-currentCenter1[1]),2) +\
                     pow(abs(eachpoint[2]-currentCenter1[2]),2)
        distance2 = pow(abs(eachpoint[3]-currentCenter2[3]),2) + pow(abs(eachpoint[1]-currentCenter2[1]),2) +\
                     pow(abs(eachpoint[2]-currentCenter2[2]),2)
        distance3 = pow(abs(eachpoint[3]-currentCenter3[3]),2) + pow(abs(eachpoint[1]-currentCenter3[1]),2) +\
                     pow(abs(eachpoint[2]-currentCenter3[2]),2)

		# 将该点指派到离它最近的质心所在的簇
        mindis = min(distance1,distance2,distance3)
        if(mindis == distance1):
            group1.append(eachpoint)
        elif(mindis == distance2):
            group2.append(eachpoint)
        else:
            group3.append(eachpoint)

	# 指派完所有的点后，更新每个簇的质心
    for c,g in [[currentCenter1,group1],[currentCenter2,group2],[currentCenter3,group3]]:
        c = [ \
                    sum([eachpoint[3] for eachpoint in group1])/len(g),\
                    sum([eachpoint[1] for eachpoint in group1])/len(g),\
                    sum([eachpoint[2] for eachpoint in group1])/len(g)\
                    ]

	# 记录该次对质心的更新
    center1.append(currentCenter1)
    center2.append(currentCenter2)
    center3.append(currentCenter3)

#print(group1)
#print(group2)
#print(group3)

print(len(group1))
print(len(group2))
print(len(group3))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for g,c,m in[[group1,'r','o'],[group2,'g','^'],[group3,'b','o']]:
    x=[eachpoint[3] for eachpoint in g]
    y=[eachpoint[1] for eachpoint in g]
    z=[eachpoint[2] for eachpoint in g]
    ax.scatter(x,y,z, c=c, marker=m)

plt.show()
