n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
    print(sum, end = " ")
    count += 1
    a = b
    b = sum
    sum = a + b
'''
Output :
Enter the value of 'n': 10
Fibonacci Series:  0 1 1 2 3 5 8 13 21 34 
'''
