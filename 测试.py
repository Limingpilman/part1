'''
 * @Author: codeman 
 * @Date: 2019-03-25 21:25:30 
 * @Last Modified by:   codeman 
 * @Last Modified time: 2019-03-25 21:25:30 
 * @funtion: 从长度为1000的列表中找出最大的十个数，按升序排序
'''
import random
import time

t = []
for i in range(1000):
    t.append(random.randint(1,10000))
i = 10
p = []
for i in range(10):
    p.append(t[i])
start = time.clock()
# signal = 1
# while i < 1000:                     #方案一、建立一个输出列表，找到最小值与原列表中的值进行比较，如果大于，就放进去，
#     if signal == 1:                 #保证输出列表中，最小值都比原数组中的其他值大
#         min_ = 0
#         for j in range(1, 10):          #找出输出列表中的最小值
#             if p[j] < p[min_]:
#                 min_ = j
#     if p[min_] < t[i]:              #比较原列表中的待检测值和最小值，如果大于最小值，说明满足条件，把待检测值输入列表替换原最小值
#         p[min_] = t[i]
#         signal = 1
#     else:
#         signal = 0
#     i+=1
for i in range(1,10):               #插入排序
    if p[i] < p[i-1]:
        j = i-1
        ex = p[i]
        while j >=0 and p[j] > ex:  
            p[j+1] = p[j]
            j = j-1
        p[j+1] = ex
while i < 1000:
    if p[0] >= t[i]:
        i+=1
        continue                    #方案二、先建立一个有序列表，然后根据大小，将待测值插入到有序列表中，最后生成一个有序列表输出
    for j in range(10):             #根据大小插入待测值
        if j == 9 and p[9] < t[i]:
            p[9] = t[i]
            break
        if p[j] >= t[i]:
            p[j-1] = t[i]
            break
        else:
            p[j] = p[j+1]
    i+=1
end = time.clock()
print(t,'\n')
print(p)
print('time:',end - start)