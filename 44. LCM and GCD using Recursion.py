def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return int((a*b)/gcd(a,b))
    
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("GCD is:",gcd(a,b))
print("LCM is:",lcm(a,b))

'''
Enter first number:20
Enter second number:35
GCD is: 5
LCM is: 140
'''
