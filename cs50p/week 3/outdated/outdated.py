month_ = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        input_ = input("Date: ").strip()


        if ',' in input_:
            parts = input_.split(',')
            year = parts[1].strip()
            month_day_part = parts[0].split()

            if month_day_part[0] in month_:
                month_num = month_.index(month_day_part[0]) + 1
                day = month_day_part[1].strip()
            else:
                raise ValueError
            if int(day) <=31 and month_num <= 12:
                print(f'{year}-{month_num:02}-{int(day):02}')
            else:
                raise ValueError


        elif '/' in input_:
            parts = input_.split('/')
            month_num = int(parts[0])
            day = int(parts[1])
            year = int(parts[2])

            if 1 <= month_num <= 12 and 1 <= day <= 31:
                print(f'{year:04}-{month_num:02}-{day:02}')
            else:
                raise ValueError
        else:
            raise ValueError

        break

    except ValueError:
        pass
