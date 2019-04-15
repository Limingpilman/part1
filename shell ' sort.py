# import random

t = [77, 14, 16, 32, 32, 70, 15, 46, 71, 93, 95, 67, 97, 60, 30, 18, 17, 76, 49, 9, 91, 43, 65, 41, 3, 82, 12]
gin = len(t)
while gin >= 2:
    gin = gin//3+1
    for i in range(gin,len(t)):
        if t[i-gin] > t[i]:
            j = i - gin
            ex = t[i]
            while j >= 0 and t[j] > ex:
                t[j+gin] = t[j]
                j = j - gin
            t[j+gin] = ex
print(t)
