class my_class():
    def find_indices(self,a,sum):
        for i in range (0,len(a)-1):
            for j in range (i+1,len(a)):
                if(a[i]+a[j]==sum):
                    print('(',i,',',j,')')
                    
n=int(input('Enter size:'))
a=[]
print('Enter elements:\n')
for i in range (0,n):
    x=int(input())
    a.append(x)

sum=int(input('Enter Sum to be found:'))

print('\nIndices:')
print(my_class().find_indices(a,sum))



