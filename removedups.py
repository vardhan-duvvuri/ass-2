def remove_data(a):
    n=len(a)
    b=[]
    for i in range(0,n):
        if a[i] not in b:
            b.append(a[i])
    return b
def get_data():
	nums=[]
	while True:
		a=int(raw_input("Enter a number (-1 to exit) : "))
		if a==-1:
			break
		nums.append(a)
	return nums

if __name__=='__main__':
	nums=get_data()
	print "Input data is : ",nums
	print "The data after removing duplicates is : ",remove_data(nums)
