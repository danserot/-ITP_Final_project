import re

def validate_name(name):
    return bool(re.match(r"^[A-Za-zA-Яа-я]{2,30}$", name))

def validate_positive_number(value):
    try:
        return float(value) >= 0
    except ValueError:
        return False

