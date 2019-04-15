import random

t =[]
for i in range(40):
    t.append(random.randint(1,200))
print(t)

def merge(t):
    if len(t) < 2:
        return t
    else:
        t_left = t[0 : len(t)//2]
        t_right = t[len(t)//2 : len(t)]
        return mergeSort(merge(t_left), merge(t_right))

def mergeSort(t_left, t_right):
    t_put = []
    while len(t_left) > 0 and len(t_right) > 0:
        if t_left[0] > t_right[0]:
            t_put.append(t_right.pop(0))
        else:
            t_put.append(t_left.pop(0))
    while(len(t_left)):
        t_put.append(t_left.pop(0))
    while(len(t_right)):
        t_put.append(t_right.pop(0))
    return t_put

print(merge(t))