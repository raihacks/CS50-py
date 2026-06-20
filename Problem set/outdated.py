months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        dates = input("Date: ").strip()
        try:
            if "/" in dates:
                month, day , year = dates.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
            else:
                nmonth, rest = dates.split(" ", 1)
                if nmonth not in months:
                    raise ValueError
                day, year = rest.split(",")
                day = int(day.strip())
                year = int(year.strip())
                month = months.index(nmonth) +1
            if not(1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break
        except(ValueError, IndexError):
            pass

main()