
from datetime import date, timedelta
import calendar

def calculate_age(birth_date: date) -> dict:
    """
    birth_date: date object represents the birthday
    returns a dictionary containing the age in years and time till next birthday
    """
    today = date.today()

    age = today.year - birth_date.year

    birthday_this_year = (birth_date.month, birth_date.day)

    if (today.month, today.day) < birthday_this_year:
        age -= 1

    next_year = today.year

    if (today.month, today.day) >= birthday_this_year:
        next_year += 1

    if birth_date.month == 2 and birth_date.day == 29:
        day = 29 if calendar.isleap(next_year) else 28
        next_birthday = date(next_year, 2, day)
    else:
        next_birthday = date(
            next_year,
            birth_date.month,
            birth_date.day
        )
    days_till_birthday = (next_birthday - today).days
    output = {"age": age,
              "time_till_birthday": days_to_months(today, days_till_birthday)
    }
    return output





def days_to_months(start: date, days: int) -> tuple:
    """
    Convert a number of days after `start` into months and remaining days.
    """
    end = start + timedelta(days=days)

    months = (end.year - start.year) * 12 + end.month - start.month

    if end.day < start.day:
        months -= 1

    total_months = start.year * 12 + start.month - 1 + months

    year, month_index = divmod(total_months, 12)
    month = month_index + 1

    day = min(
        start.day,
        calendar.monthrange(year, month)[1]
    )

    intermediate = date(year, month, day)

    remaining_days = (end - intermediate).days

    return months, remaining_days
    
