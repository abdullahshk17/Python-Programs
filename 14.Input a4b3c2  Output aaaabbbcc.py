def fun(s):
    output=''
    for x in s:
        if x.isalpha():
            output=output+x
            previous=x
        else:
            output=output+previous*(int(x)-1)
    return output
s=input("Enter Some String:")  #a4b3c2
print(fun(s))    #aaaabbbcc
