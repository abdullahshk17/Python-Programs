def leapyear(year):
    if ((year%400==0) or (year%4==0 and year%100!=0)):
        return True
    else:
        return False
n=int(input()) 
print(leapyear(n))
