w=input("Enter word to search for vowels: ")  
s=set(w)
v={'a','e','i','o','u'}
d=s.intersection(v)
print("The different vowel present in",w,"are",list(d))

'''
Enter word to search for vowels: Learning Python is very easy
The different vowel present in Learning Python is very easy are ['i', 'a', 'e', 'o']
'''
