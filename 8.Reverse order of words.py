s=input() #Learning Python is very easy!!
l=s.split()
print(l)      #['Learning', 'Python', 'is', 'very', 'easy!!']
for i in range(len(l)):
    res=l[::i-len(l)] 
print(res)     #['easy!!', 'very', 'is', 'Python', 'Learning']
for i in range(len(res)):
    print(res[i],end=" ")    #easy!! very is Python Learning
