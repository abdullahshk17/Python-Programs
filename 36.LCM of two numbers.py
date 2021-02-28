a=int(input())
b=int(input())
for i in range(1 , a*b +1):
    if (i%a==0 and i%b==0):
        print("LCM of a number is ",i)
        break
'''Output:
30
50
LCM of a number is  150'''
