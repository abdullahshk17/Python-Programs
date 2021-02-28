def count(s):
    l=sorted(list(set(s)))
    for i in range(len(l)):
        new=s.count(l[i])
        print("{}-{}".format(l[i],new),end=" ")     #A-3 B-4 C-3 D-1 E-1   
s=input() #ABCABCABBCDE
count(s)
