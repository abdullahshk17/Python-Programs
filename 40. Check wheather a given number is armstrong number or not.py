num = int(input())
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
'''    
Output:
153
153 is an Armstrong number
1999
1999 is not an Armstrong number
'''
