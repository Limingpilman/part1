import random

t = [17, 53, 41, 36, 54, 11, 63, 15, 55, 88, 46, 42, 10, 81, 35, 87, 87, 50, 75, 67, 53, 86, 92, 37, 100, 5, 90, 85, 67, 21, 33, 4, 33, 92, 82, 77, 97, 9, 36, 45]

for i in range(1,40):
    if t[i] < t[i-1]:
        j = i-1
        ex = t[i]
        while j >=0 and t[j] > ex:
            t[j+1] = t[j]
            j = j-1
        t[j+1] = ex
p = t.copy()
p.sort()
print(p,'\n')
print(t)
