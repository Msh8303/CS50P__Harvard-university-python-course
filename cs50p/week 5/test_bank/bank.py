def main():
    input_ = input ("Greeting: ")
    print(value(input_))

def value(input_):
    input_ = input_.lower()
    splited = input_.split()

    if splited[0] == 'hello' or input_.startswith('hello'):
        return 0
    elif splited[0].startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
