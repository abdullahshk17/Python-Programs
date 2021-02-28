def find_all_indexes(input_str, search_str):
    l1 = []
    length = len(input_str)
    index = 0
    while index < length:
        i = input_str.find(search_str, index)
        if i == -1:
            return l1
        l1.append(i)
        index = i + 1
    return l1
s=input()    #abbababababacdefg
sub=input()  #a

res=find_all_indexes(s,sub)
for i in range(len(res)):
    print("{} Found at position : {} ".format(sub,res[i]))

'''
Output:abbababababacdefg
a
a Found at position : 0 
a Found at position : 3 
a Found at position : 5 
a Found at position : 7 
a Found at position : 9 
a Found at position : 11 
'''
