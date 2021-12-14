def leap_year(year):  # Definition eines Schaltjahres
    if year % 400 == 0:
        return True
    else:
        if year % 4 == 0:
            if year % 100 == 0:
                return False
            else:
                return True
        else:
            return False


def days_in_month(year, month):  # Definition der Anzahl der Tage in einem Monat
    if month == 2:
        if leap_year(year) == True:
            return 29
        else:
            return 28
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31


def week_day(year, day, month):  # Definition eines Wochentages
    y = year % 100
    c = year // 100
    if month == 5:
        k = 0
    elif month == 8:
        k = 1
    elif month == 2:
        if leap_year(year) == True:
            k = 1
        else:
            k = 2
    elif month in (11, 3):
        k = 2
    elif month == 6:
        k = 3
    elif month in (9, 12):
        k = 4
    elif month in (4, 7):
        k = 5
    elif month == 1:
        if leap_year(year) == True:
            k = 5
        else:
            k = 6
    elif month == 10:
        k = 6
    d = (day + k + y + y // 4 - 2 * (c % 4)) % 7
    return d


def month_name(m):  # Definition des Monatsnamen
    if m == 1:
        return "Januar"
    if m == 2:
        return "Februar"
    if m == 3:
        return "Maerz"
    if m == 4:
        return "April"
    if m == 5:
        return "Mai"
    if m == 6:
        return "Juni"
    if m == 7:
        return "Juli"
    if m == 8:
        return "August"
    if m == 9:
        return "September"
    if m == 10:
        return "Oktober"
    if m == 11:
        return "November"
    if m == 12:
        return "Dezember"


def calendar(year):  # Ausgabe des Kalenders
    W = 0
    for m in range(1, 13):
        s = month_name(m) + ' ' + str(year)
        print('{:^23}'.format(s))
        print('KW', 'SO', 'MO', 'DI', 'MI', 'DO', 'FR', 'SA')
        for day in range(1, days_in_month(year, m) + 1):
            t = week_day(year, day, m) * ' ' + str(day)
            print(W, t)
            W += 1
        print()


calendar(2017)
