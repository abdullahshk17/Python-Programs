import fractions
print("GCD =",fractions.gcd(int(input()) , int(input())))
'''Output:
60
48
GCD = 12'''
#OR
a=int(input())
b=int(input())
while a%b !=0 :
    rem=a%b
    a=b
    b=rem
print("GCD/HCF =",b)
'''Output:
25
15
GCD/HCF = 5'''
