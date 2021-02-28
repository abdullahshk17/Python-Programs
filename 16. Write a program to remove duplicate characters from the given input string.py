def fun(s):
    l=[]
    for x in s:
        if x not in l:
            l.append(x)
            output=''.join(l)
    return output
s=input("Enter Some String:")  #Hello Mr
print(fun(s))  #Helo Mr
