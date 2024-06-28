from datetime import date

def solution(a, b):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    today = date(2016, a, b)
    day = today.weekday()
    return days[day]