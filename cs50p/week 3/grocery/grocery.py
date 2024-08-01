
my_dict = {}

while True:
    try:

        input_ = input().strip()
        input_ = input_.upper()
        my_dict[input_] = my_dict.get(input_,0) + 1


    except EOFError:
        break

my_dict = dict(sorted(my_dict.items(), key=lambda item: item[0]))

for key, value in my_dict.items():
    print (value, key)

