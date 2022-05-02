array=[1,2,3,4,5,6,7,8,9,10]

def bin_search(a,low,high,x):
    if(low<=high):
        mid=(low+high)//2

        if(a[mid]==x):
            return mid
        elif(a[mid]>x):
            return bin_search(a,low,mid-1,x)
        else:
            return bin_search(a,mid+1,high,x)

    else:
        return -1

ans=bin_search(array,0,9,8)
if(ans==-1):
    print("Not Found")
else:
    print(f"Found at index {ans}")