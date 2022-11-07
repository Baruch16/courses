import random
import matplotlib.pyplot as plt

N = 10000
x = [0] * N
y = [0] * N
a = [0] * N
for i in range(N-1):
    dice = random.random()
    if dice > 0.3 and dice < 0.6:
    	z = x
    	w = y
    	r = a
    elif dice > 0.6:
       	z = y
       	w = x
       	r = a
    else:
     	z = a	
     	w = x	
     	r = y
    dice = random.random()
    if dice > 0.5:
    	z[i+1] = z[i]+1	
    	w[i+1] = w[i]	
    	r[i+1] = r[i]
    else:
    	z[i+1] = z[i]-1	
    	w[i+1] = w[i]
    	r[i+1] = r[i]
we= plt.subplot(1,1,1,projection = "3d") 
we.plot(y,x,z)
plt.show()
