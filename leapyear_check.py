def leap_year_check(year):
    if year%4 == 0 :
        if year%100 == 0 and year%400 == 0:
             leap = True
        elif year%100 == 0 and year%400 != 0:
             leap = False
        elif year%100 != 0:
             leap = True
    else :
        leap = False
    return leap

year = int(input("Enter the year to check:"))

print(leap_year_check(year))