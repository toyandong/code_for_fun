#-------------------------------------------------------------------------------
# Name:        e3_5
# Purpose:
#
# Author:      yandong
#
# Created:     30/10/2013
# Copyright:   (c) yandong 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import pylab as plt

N=3
w=[]
d=[]
C=1
LOOP=2
couter=0
data=[[-1,-1,1],[0,0,1],[1,1,1]]
label=[0,1,2]
dar=np.array(data)
#init
for i in range(N):
    w+=[[0]*N]
    d+=[0.0]
print(w,len(w),d,len(d))

flag=0
while couter < LOOP :
    couter+=1
    for i in range(len(data)):
        print("data ", i, label[i])
        d[label[i]] =sum(w[label[i]]*dar[i])
        for j in range(N):
            d[j] =sum( w[j]*dar[i])
            if(label[i]!=j and (d[j] >= d[label[i]])):
                print("COMPARE ",j,label[i],d[j], d[label[i]])
                flag=1
                w[j] = w[j] -C*dar[i]
        if flag==1 :
            w[label[i]] = w[label[i]] + C*dar[i]
            flag=0
        print(w, d)

for i in range(N):
    print("第",i,"类 ",w[i])

fig = plt.figure()
ax = fig.add_subplot()
plt.xlim([-2,2])
plt.ylim([-2,2])
c='rbgrgbrgbrgb'
m='o^o^o^o^o^o^'
for i in range(3):
    print(i, data[i])
    plt.plot(data[i][0], data[i][1], '-', color=c[label[i]], marker=m[label[i]])

plt.show()









