def is_leap(year):
    return year%400==0 or (year%4==0 and not year%100==0)

def days_in_month(month, year):
           # J   F   M   A   M   J   J   A   S   O   N   D
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month==1 and is_leap(year): return 29
    return days[month]

def days_gen(month, year):
    while 1:
        yield (month, year, days_in_month(month, year))
        if month == 11: year += 1
        month = (month + 1) % 12
        

# from a monday day (1st of jan 1900), days % 7 == 6 -> Sunday
def count_first_sundays():
    day = 1 #tuesday (worked out from 365 % 1)
    total = 0
    for (month, year, days) in days_gen(0, 1901):
        if year > 2000: return total
        day = (day + days)%7
        if day == 6:
            total += 1

# could have used DOOMSDAY alg too
print count_first_sundays()
