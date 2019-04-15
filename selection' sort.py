import random

t =[]
for i in range(40):
    t.append(random.randint(1,200))

for i in range(39):
    LP = i
    for j in range(i+1,40):
        if t[LP] > t[j]:
            LP = j
    ex = t[i]
    t[i] = t[LP]
    t[LP] = ex
print(t)