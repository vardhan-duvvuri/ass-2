def sum(a,i,j,k):
    s=a[i]+a[j]
    if s == k:
        print "a["+str(i)+"] + a["+str(j)+"] = "+str(k)
        if i < j-2:
            i+=1
            j-=1
            sum(a,i,j,k)
    elif s > k:
        j-=1
        sum(a,i,j,k)
    else:
        i+=1
        sum(a,i,j,k)    
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
	i=0
	j=len(nums)-1
	k=int(raw_input("Enter the k value : "))
	sum(nums,i,j,k)
