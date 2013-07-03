import math
def merge(a,b):
    a_i=0
    b_i=0
    n=[]
    while a_i <= len(a)-1 and b_i <= len(b)-1:
        if a[a_i]<b[b_i]:
            n.append(a[a_i])
            a_i+=1
        else:
            n.append(b[b_i])
            b_i+=1
    if a_i <= len(a)-1:
        n.extend(a[a_i:len(a)])
    if (b_i <= len(b)-1):
        n.extend(b[b_i:len(b)])
    return n
def replace(original,replace,i,j):
    original[i:j+1]=replace[0:]
    return original
def merge_iter(nums):
    n=len(nums)
    #print n
    no_levels= int(math.ceil(math.log(n,2.0)))
    #print "\nThe total  no.of levels we have to process is ",no_levels
    for i in range(no_levels) :
        max_pro_size = 2**i
        #print "\nThe max size of the problem is %d at %d level" % (max_pro_size,i)
        no_merges=int(math.ceil(n/(2.0*max_pro_size)))
        #print "The no.of merges needed are %d at %d level" % (no_merges,i)
        for j in range(no_merges):
            s_i=2*max_pro_size*j
            m_i=s_i+max_pro_size
            e_i=m_i+max_pro_size-1
            #print "The comparisions at level %d are nums[%d:%d] and nums[%d:%d] " % (i,s_i,m_i-1,m_i,e_i)
            if n-1 < m_i:
                e_i=n-1
                #print "The comparisions at level %d are nums[%d:%d] and nums[%d:%d] \n" % (i,s_i,m_i-1,m_i,e_i)
                
            else:
                if n-1 < e_i:
                    e_i=n-1
                    #print "The comparisions at level %d are nums[%d:%d] and nums[%d:%d] \n" % (i,s_i,m_i-1,m_i,e_i)
                    
                else:
                    pass
                    #print "The comparisions at level %d are nums[%d:%d] and nums[%d:%d] " % (i,s_i,m_i-1,m_i,e_i)
            #print nums[s_i:m_i],nums[m_i:e_i+1]
                num1=merge(nums[s_i:m_i],nums[m_i:e_i+1])
        #print num1
                num2=replace(nums,num1,s_i,e_i)
    nu=num2
    return nu
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
	nums=merge_iter(nums)
	print "Output data is : ",nums
