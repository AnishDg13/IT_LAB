class q1:
    def i2b(self,temp):
        bin=''
        while(temp>0):
            rem=temp%2
            bin=str(rem)+''+bin
            temp=temp//2
        return bin

print('Enter size of array:')
n=int(input())
a=[]
print(f'Enter {n} numbers:\n')
for i in range(0,n):
    x=int(input())
    if(x in a):
        print('Only distinct numbers allowed.')
        exit()
    a.append(x)
a.sort()
total=2**len(a)
for i in range (0,total):
    bin=q1().i2b(i)
    temp_arr=[]
    for j in range (0,len(bin)):
        if bin[j]=='1':
            temp_arr.append(a[len(a)-len(bin)+j])
    print(temp_arr)

