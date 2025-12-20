#x=int(input("enter x: "))
#ans=10/x
#print(f"{ans} = ans")

try:
    x=int(input("enter x : "))
    ans=10/x
except ZeroDivisionError :
    print(f"division by zero is not allowed")
except ValueError:
    print("invalid input")
else:
    print(f"ans = {ans}")
# final keyword always exexcutes irrespective of the error being thrown or not
finally:
    print("end of program")
print("")