def year(x):
    if x%4 == 0:
        print (f"{x} is leap year")
        return 1
    else:
        print(f"{x} is not leap year")
        return 0
      
      
def month(y):
    if y == 1:
        print (f"{y} has 31 days")
    elif y == 3:
        print (f"{y} has 31 days")
    elif y == 5:
        print (f"{y} has 31 days")
    elif y == 7:
        print (f"{y} has 31 days")
    elif y == 8:
        print (f"{y} has 31 days")
    elif y == 12:
        print (f"{y} has 31 days")
        #feb is leap year
    elif y == 2:
        z=28
        z = z+x
        print (f"{y} has {z} days")
    elif y == 4:
        print (f"{y} has 30 days")
    elif y == 6:
        print (f"{y} has 30 days")
    elif y == 9:
        print (f"{y} has 30 days")
    elif y == 10:
        print (f"{y} has 30 days")
    elif y == 11:
        print (f"{y} has 30 days")
        
        
x = year(2021)
month(7)
