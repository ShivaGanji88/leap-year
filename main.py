#leap year
#coding practise

year = int(input("which year do you want to check: "))

if year % 4 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Leap year")
elif year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")    
