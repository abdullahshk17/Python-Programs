def fun(s):
    s1=s2=output=''
    for x in s:
        if x.isalpha():
            s1=s1+x
        else:
            s2=s2+x
    for x in sorted(s1):
        output=output+x
    for x in sorted(s2):
        output=output+x
    return output
s=input("Enter Some String:")  #C4A1B3
print(fun(s))  #ABC134
