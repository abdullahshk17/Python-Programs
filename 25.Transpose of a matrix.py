l=[]
n=int(input())
for i in range(n):
    l.append(list(map(int,input().split( )))[:n])
trans=zip(*l)
#print(trans)
for i in trans:
    print(list(i))
'''Outpit:
3
1 2 3
8 20 47
45 9 1
[(1, 8, 45), (2, 20, 9), (3, 47, 1)]
[1, 8, 45]
[2, 20, 9]
[3, 47, 1]
'''
