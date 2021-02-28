def alter(s1,s2):
    l1=len(s1)
    l2=len(s2)
    l=max(l1,l2)
    res=''
    for i in range(l):
        if i<len(s1):
            res+=s1[i]
        if i<len(s2):
            res+=s2[i]
    return res
s1=input()  #Raj
s2=input()  #Rahul
print(alter(s1,s2))  #RRaajhul
