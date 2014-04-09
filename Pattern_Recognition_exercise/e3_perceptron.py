#-------------------------------------------------------------------------------
# Name:        閹扮喓鐓￠崳銊х暬濞?
# Purpose:
#
# Author:      yandong
#
# Created:     30/10/2013
# Copyright:   (c) yandong 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#鏁版嵁
data=[[0,0,0,1],[1,0,0,1], [1,0,1,1], [1,1,0,1] \
        ,[0,0,-1,-1], [0,-1,-1,-1], [0,-1,0,-1], [-1,-1,-1,-1]]
#w1=1, w2=-1
label=[1,1,1,1,-1,-1,-1,-1]

def perceptron(data,label,nmd=1,cyc=10):
    '''
    data is {xi}
    label should be in (-1,1)
    '''
    dar=np.array(data)
    m,n=dar.shape
    print(m,n)
    #w=np.random.random_sample(n) #鍒濆鍖杦
    w=np.array([0,0,0,0])
    for ic in range(cyc): #杩涜杩唬鐨勬鏁?
        for i in range(m):
            print("sum",i,w,dar[i],label[i],sum(dar[i]*w))
            if sum(dar[i]*w)<=0: #濡傛灉鍒嗙被閿欒杩涜w鐨勬洿鏂?
                w=w+nmd*dar[i]
                print("new",w)
    return w

print (perceptron(data,label))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
c='ry'
m='o^'
for i in [0,1,2,3]:
    ax.scatter(data[i][0],data[i][1],data[i][2], c=c[0], marker=m[0])
for i in [4,5,6,7]:
    ax.scatter(-data[i][0],-data[i][1],-data[i][2], c=c[1], marker=m[1])

x=np.linspace(-2,2,num=20)
y=np.linspace(-2,2,num=20)
x, y = np.meshgrid(x, y)
z=(2*x-2*y+1)/2
#
#z=x**2+y**2
print(z)

ax.plot_surface(x,y,z,rstride=4, cstride=4, color='b')
ax.set_zlim3d(-2,2)
plt.show()