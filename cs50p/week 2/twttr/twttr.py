input_ = input("Input: ")
vowels = ['i','e','o','u','a','A','E','O','U','I']
len_ = len(input_)
output_ = ''
for char in input_:
    if char not in vowels:
        output_ += char


print(f'Output: {output_}')