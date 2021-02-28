def lcm_gcd(a,b):
    for i in range(1 , a*b +1):
        if (i%a==0 and i%b==0):
            print("LCM of a number is ",i)
            break
    while a%b !=0 :
        rem=a%b
        a=b
        b=rem
    print("GCD/HCF =",b)
a=int(input())
b=int(input())
lcm_gcd(a,b)

''' 
25
15
LCM of a number is  75
GCD/HCF = 5
'''
