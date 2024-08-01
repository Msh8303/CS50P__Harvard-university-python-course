import inflect

p = inflect.engine()
names =[]
while True:
    try:
        input_ = input('Name: ').strip()

        names.append(input_)
    except EOFError:
        print()
        print("Adieu, adieu, to", p.join(names))
        break