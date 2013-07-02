import math
def make_heap(nums):
    n=len(nums)
    for i in range(int(math.ceil((n-2)/2)),-1,-1):
        max_heap(nums,i)
def max_heap(nums,i):
    l=(2*i)+1
    if l<len(nums) and nums[l]<nums[i]:
        small=l
    else:
        small=i
    if l+1<len(nums) and nums[l+1]<nums[small]:
        small=l+1
    if small !=i:
        temp=nums[i]
        nums[i]=nums[small]
        nums[small]=temp
        max_heap(nums,small)
def sort(temp):
    m=len(d[1])
    make_heap(temp)
    n.append(temp[0])
    print n
    for j in range(0,m):
        for i in range(0,len(d)):
            if len(n)<m*len(d):
                if temp[0] == d[i][j]:
                    if temp[0] != d[i][m-1]:
                        temp[0]=d[i][j+1]
                        sort(temp)
                    else:
                        temp.remove(temp[0])
                        sort(temp)
                else:
                    exit
    return n
a=[13,14,15,16]
b=[9,10,11,12]
c=[5,6,7,8]
e=[1,2,3,4]
d=[a,b,c,e]
temp=[]
n=[]
j=0
print "Input array is : ",d
for i in range(0,len(d)):
    temp.append(d[i][j])
x=sort(temp)
print "output array is : ",x
