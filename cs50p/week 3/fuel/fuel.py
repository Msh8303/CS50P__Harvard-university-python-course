

while True:

    try:
        input_ = input('Fraction: ')
        numerator, denomerator = input_.split('/')
        numerator = int(numerator)
        denomerator = int(denomerator)
        if denomerator == 0:
            raise ZeroDivisionError
        if numerator > denomerator:
            raise ValueError
        result = (numerator / denomerator) * 100
        result = round(result)
        if result <= 1:
            print('E')
        elif result >= 90:
            print('F')
        else:
            print(f'{result}%')

        break
    except ValueError:
        continue
    except ZeroDivisionError:
        continue









