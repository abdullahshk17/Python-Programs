n=[20,21,17,4,100]
n.reverse()
print("Reverse:",n) #[100, 4, 17, 21, 20]
n.sort()
print("Ascending order:",n) #[4, 17, 20, 21, 100]
n.sort(reverse=True)  #[100, 21, 20, 17, 4]
print("Descending order:",n)
