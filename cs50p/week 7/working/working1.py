import re

def convert(input_):
    pattern1 = r"\b(?:0?[1-9]|1[0-2]):[0-5][0-9] (?:AM|PM) to (?:0?[1-9]|1[0-2]):[0-5][0-9] (?:AM|PM)\b"
    pattern2 = r"\b(?:[01]?[0-9]|2[0-4]):[0-5][0-9] to (?:[01]?[0-9]|2[0-4]):[0-5][0-9]\b"

    def convert_time_12_to_24(time_str, suffix):
        hour, minute = map(int, time_str.split(':'))
        if suffix == 'PM' and hour < 12:
            hour += 12
        elif suffix == 'AM' and hour == 12:
            hour = 0
        return f'{hour:02}:{minute:02}'

    def convert_time_24_to_12(time_str):
        hour, minute = map(int, time_str.split(':'))
        suffix = 'AM' if hour < 12 else 'PM'
        if hour > 12:
            hour -= 12
        elif hour == 0:
            hour = 12
        return f'{hour:02}:{minute:02} {suffix}'

    if re.match(pattern1, input_):
        start_t, end_t = map(str.strip, input_.split("to"))
        start_time, start_suffix = start_t.split()
        end_time, end_suffix = end_t.split()
        start_time_24 = convert_time_12_to_24(start_time, start_suffix)
        end_time_24 = convert_time_12_to_24(end_time, end_suffix)
        return f'{start_time_24} to {end_time_24}'

    elif re.match(pattern2, input_):
        start_t, end_t = map(str.strip, input_.split("to"))
        start_time_12 = convert_time_24_to_12(start_t)
        end_time_12 = convert_time_24_to_12(end_t)
        return f'{start_time_12} to {end_time_12}'

    else:
        raise ValueError("Invalid input format")

try:
    input_ = input("Hours: ")
    print(convert(input_))
except ValueError as e:
    print(e)
