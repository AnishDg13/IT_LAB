class q3:
    def power(self,a,b):
        if(b==0):
            return 1
        else:
            return a*q3().power(a,b-1)
m=int(input('Enter number:'))
n=int(input('Enter exponent:'))
print('Result:',q3().power(m,n))




