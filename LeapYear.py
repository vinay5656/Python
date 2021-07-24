print("Enter an year you want to check is it leap year")
year = int(input("Enter an year"))

if int(year%4) == 0 and int(year%100)!=0 or int(year%400)==0:
    print(f"{year} is leap year")
else :
    print(f"{year} is not leap year")