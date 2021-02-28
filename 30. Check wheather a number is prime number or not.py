import math
n=int(input())
flag = 0
#for i in range(2,(n/2)+1):
for i in range(2,int(math.sqrt(n))+1):
    if(n%i==0):
        flag=1
        break
if(flag==0):
    print("{} is a prime number".format(n))
else:
    print("{} is not a prime number".format(n))
