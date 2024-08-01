


def convert(time):
    hour, minute = time.strip().split(":")
    time_ = float(hour) + float(minute)/60
    return time_


def main():

    dic = [
        {"meal" : "breakfast time", "start" : 7 , "end" : 8},
        {"meal" : "lunch time", "start" : 12 , "end" : 13},
        {"meal" : "dinner time", "start" : 18 , "end" : 19}
    ]
    time = input("What time is it? ")
    time = convert(time)
    for time__ in dic:
        if time >= float(time__['start']) and time <= float(time__['end']):
            print(time__['meal'])
        else:
            continue



if __name__ == "__main__":
    main()