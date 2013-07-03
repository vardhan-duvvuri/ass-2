def sum(a,b,i,j,k):
    if i<len(a) and j>=0:
        s=a[i]+b[j]
        if s == k:
            print "a["+str(i)+"]+b["+str(j)+"]="+str(k)
        elif s < k:
            i+=1
            sum(a,b,i,j,k)
        else:
            j-=1
            sum(a,b,i,j,k)
    else:
        print "Element not found"
def get_data():
	nums=[]
	while True:
		a=int(raw_input("Enter a number (-1 to exit) : "))
		if a==-1:
			break
		nums.append(a)
	return nums

if __name__=='__main__':
    print "Enter elements to Array A:"
    a=get_data()
    print "Enter elements to Array B:"
    b=get_data()
    print "Input data is : ",a,b
    i=0
    j=len(b)-1
    k=int(raw_input("Enter the k value : "))
    sum(a,b,i,j,k)
