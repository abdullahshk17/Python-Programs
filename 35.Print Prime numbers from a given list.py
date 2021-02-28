num=list(map(int,input().split()))
prime=[]
for i in range(len(num)):
    factor=0
    for j in range(2,num[i]):
        if num[i]%j==0 :
            factor+=1
            break
    if factor==0:
        prime.append(num[i])
if len(prime)>0:
    print("List of prime numbers from a list is",prime)
else:
    print("No prime number in a given list")

'''
17 5 26 18 31
List of prime numbers from a list is [17, 5, 31]
'''
