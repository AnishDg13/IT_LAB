a=float(input("Enter 1st number:"))
b=float(input("Enter 2nd number:"))
print("\n1.Enter 1 to add.")
print(f"\n1.Enter 2 subtract {b} from {a}.")
print("\n1.Enter 3 to multiply.")
print(f"\n1.Enter 4 to divide {a} by {b}.")
choice=int(input("Enter choice:"))
r=0.0

if choice==1:
	r=a+b
elif choice==2:
	r=a-b
elif choice==3:
	r=a*b
else:
	r=a/b

print("Result: ",r)
