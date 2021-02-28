s=input() #Learning Python is easy
l=s.split()
new=[]
for i in range(len(l)):
    new.append(l[i][::-1])
print(new)   #['gninraeL', 'nohtyP', 'si', 'ysae']
for i in range(len(new)):
    print(new[i],end=" ")   #gninraeL nohtyP si ysae 
