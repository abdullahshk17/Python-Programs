import math
n=list(map(int,input()))
#print(n)
c=0
sum=0
for i in range(len(n)):
    c+=1
for i in range(c):
    sum=sum+math.factorial(n[i])
print(sum)
sum=[int(i) for i in str(sum)]
if(sum==n):
    print("Strong Number")
else:
    print("Not a Strong Number")
