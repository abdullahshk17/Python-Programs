rec={}
n=int(input("Enter number of students: "))
i=1
while i <=n:
    name=input("Enter Student Name: ")
    marks=input("Enter % of Marks of Student: ")
    rec[name]=marks
    i=i+1
print(rec)
print("Name of Student","\t","% of marks")
for x in rec:
    print("\t",x,"\t\t",rec[x]) 

'''
Enter number of students: 3
Enter Student Name: Raj
Enter % of Marks of Student: 88
Enter Student Name: Ram
Enter % of Marks of Student: 91
Enter Student Name: Ravi
Enter % of Marks of Student: 87
{'Raj': '88', 'Ram': '91', 'Ravi': '87'}
Name of Student 	 % of marks
	 Raj 		 88
	 Ram 		 91
	 Ravi 		 87
'''
