def check_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

def main():
    year = int(input("Enter a year: "))
    check_leap_year(year)

main()