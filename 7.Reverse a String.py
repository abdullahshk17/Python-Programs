#Using Slicing
s=input("Enter Some String : ")
print("Reverse Using Slicing :",s[::-1])
    #OR
#Without using Slicing
i=len(s)-1
target=''
while i>=0:
    target=target+s[i]
    i=i-1
print("Reverse Without Using Slicing :",target)
print("Using inbuilt function :",''.join(reversed(s)))

'''
Enter Some String : Hello Mr
Reverse Using Slicing : rM olleH
Reverse Without Using Slicing : rM olleH
Using inbuilt function : rM olleH
'''
