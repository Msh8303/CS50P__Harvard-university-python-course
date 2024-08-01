import random


def main():
    level = get_level()
    score = 0
    chances = 3
    i = 10
    while i != 0:
        if chances == 3:
                x, y = generate_integer(level)
        try:


            answer = x + y
            input_answer =int(input(f'{x} + {y} = '))
            if input_answer == answer:
                score += 1
                chances = 3
                i -= 1
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print('EEE')
            chances -= 1
            pass
        if chances == 0:
            print(f'{x} + {y} = {answer}')
            chances = 3
            i -= 1
            continue

    print(score)


def get_level():
    while True:
        try:
            level_ = int(input('Level: '))
            if level_ <= 3 and level_>=1:
                return level_

        except:
            pass



def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)

    return x,y

if __name__ == "__main__":
    main()
