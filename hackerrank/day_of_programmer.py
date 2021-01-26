def get_gregorian(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def get_julian(year):
    return True if year % 4 == 0 else False

def day_of_programmer(year):
    day = 13
    if year == 1918:
        day = 26
    elif year > 1918:
        day = 12 if get_gregorian(year) else 13
    else:
        day = 12 if get_julian(year) else 13
    return f'{day}.09.{year}'

if __name__ == '__main__':

    print(day_of_programmer(1800))