import random
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def scP(p, t = 100):
    for i in range(t):
        if i ==0:
            p = {'pp1':20}
        else:
            p.update({'pp{}'.format(i+1):20})
    return p

def run_(p,N,t = 100):
    for i in range(N):
        Ness = random.randint(1,100)
        for j in range(1,t+1):
            if j == Ness:
                p['pp{}'.format(j)] = p['pp{}'.format(j)] + 1*(t-1)
            p['pp{}'.format(j)] = p['pp{}'.format(j)] -1
    return p

t, N= 100, 100000
p = {}
x = []
y = []
fig, ax = plt.subplots()
people = scP(p, t)
p_ = run_(people, N, t)
for i in range(t):
    x.append(i+1)
    y.append(p_['pp{}'.format(i+1)])
# ax.cla()
# ax.bar(x, y, color = 'g', label = 'mat')
# plt.axis([0, 100,-300,600])
y.sort()
for i in range(t):
    y[i]=y[i]/2000
ax.bar(x, y, color = 'r', label = 'm')
plt.xlabel('{}'.format(N))
plt.legend()
# plt.pause(0.1)
plt.show()