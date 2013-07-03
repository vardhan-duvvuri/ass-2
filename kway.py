import math
def make_heap(nums):
    n=len(nums)
    for i in range(int(math.ceil((n-2)/2)),-1,-1):
        max_heap(nums,i)
def max_heap(nums,i):
    l=(2*i)+1
    if l<len(nums) and nums[l]<nums[i]:
        large=l
    else:
        large=i
    if l+1<len(nums) and nums[l+1]<nums[large]:
        large=l+1
    if large !=i:
        temp=nums[i]
        nums[i]=nums[large]
        nums[large]=temp
        max_heap(nums,large)
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

def get_data():
	nums=[]
	while True:
		a=int(raw_input("Enter a number (-1 to exit) : "))
		if a==-1:
			break
		nums.append(a)
	return nums

if __name__=='__main__':
    print "Enter the data the size is multiples of 4"
    nums=get_data()
    print "Input data is : ",nums


k=len(nums)
a=nums[:k/4]
b=nums[k/4:k/4+k/4]
c=nums[(k/4+k/4):(k/4+k/4+k/4)]
e=nums[(k/4+k/4+k/4):]
#print a,b,c,e
d=[a,b,c,e]
temp=[]
n=[]
j=0
print "Input array is : ",d
if len(d[1])!=0:
    for i in range(0,len(d)):
        temp.append(d[i][j])
    x=sort(temp)
    print "output array is : ",x
else:
    print "Empty list"
