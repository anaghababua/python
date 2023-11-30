current_year=int(input("enter the current year:"))
final_year=int(input("enter the final year:"))
if(current_year<final_year):
    print("the leap year are:")
    for year in range(current_year,final_year+1):
        if(year%4==0):
            print(year)
else:
                print("no future leap years found")

