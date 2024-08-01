def main():
    input_ = input('Fraction: ')
    result = convert(input_)
    print(gauge(result))


def convert(input_):

        numerator, denomerator = input_.split('/')
        numerator = int(numerator)
        denomerator = int(denomerator)
        if denomerator == 0:
            raise ZeroDivisionError
        if numerator > denomerator:
            raise ValueError
        result = (numerator / denomerator) * 100
        result = round(result)
        return result

def gauge(result):
    if result <= 1:
        return f'E'
    elif result >= 90:
        return f'F'
    else:
        return f'{result}%'





if __name__  == '__main__':
    main()




