def fun(s):
    output=''
    for x in s:
        if x.isalpha():
            output=output+x
            previous=x
        else:
            output=output+chr(ord(previous)+int(x))
    return output
s=input("Enter Some String:")   #a4k3b2
print(fun(s))    #aeknbd
