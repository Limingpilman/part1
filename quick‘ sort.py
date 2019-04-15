import random

# t = []
# for i in range(30):
#     t.append(random.randint(1,100))
t = [3,7,2,9,1,4,6,8,10,5]
def quick(t, left, right):
    if left < right:
        i = left - 1        # i是划分标志
        x = t[right]        # 以列表最右端为基准值
        for j in range(left, right+1):
            if t[j] <= x:   # 把大于基准值的成员交换到小于基准值的成员后面，直到把基准值换过去，实现列表划分
                i+=1        # 记录小于或等于基准值的列表成员的尾端位置
                ex = t[i]
                t[i] = t[j]
                t[j] = ex
        quick(t, left, i-1) #以基准值划分左右分列表，递归排序
        quick(t, i+1, right)
    return t

print(quick(t, 0, len(t)-1))
'''
快速排序法，是通过设立基准值，将列表划分为左右两边，一边都比一边小（大）的情况，然后通过调用递归，不断重复划分过程，从而由大到小地实现排序的过程
'''