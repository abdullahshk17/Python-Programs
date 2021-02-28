import math
low=int(input())
high=int(input())
prime=[]
for num in range(low,high+1):
    factor=0
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0 :
            factor+=1
            break
    if factor==0:
        prime.append(num)
print("List of prime numbers is",prime)
