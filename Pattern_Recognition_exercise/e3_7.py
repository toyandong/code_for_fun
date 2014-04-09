import numpy as np
import pylab as plt


data=[\
    [0,0,0,1],\
    [1,0,0,1],\
    [1,0,1,1],\
    [1,1,0,1],\
    [0,0,-1,-1],\
    [0,-1,-1,-1],\
    [0,-1,0,-1],\
    [-1,-1,-1,-1]\
    ]

X=np.array(data)
m,n=X.shape
C=1
b=np.ones(m)
w=[0.0]*n
# X_sharp= (Xt*X)^-1 *Xt
XT=X.transpose()
X_sharp=np.dot(np.linalg.inv(np.dot(XT,X)),XT)
print(X_sharp)
MAX_LOOP=100
couter=0
w=np.dot(X_sharp,b)
#print(np.dot(X_sharp,b))
while couter < MAX_LOOP:
    couter+=1
    e=np.dot(X,w)-b
    abs_e=np.abs(e)
    print("LOOP ",couter,w,e,b)
    w=w+C*np.dot(X_sharp,abs_e)
    b=b+C*(e+abs_e)
    if(sum(abs_e)==0):
        print("e(%d) = 0"%couter)
        break
    if(sum(e+abs_e)==0):
        print("e(%d) < 0"%couter, e+abs_e)
        break

print(w)




