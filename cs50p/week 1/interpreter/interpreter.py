input_ = input("Expression: ")
x,y,z = input_.split()


if y == '+':
    res = float(x) + float(z)
    print(res)
elif y == '-':
    res = float(x) - float(z)
    print(res)
elif y == '*':
    res = float(x) * float(z)
    print(res)
elif y == '/':
    if int(z) != 0:
        res =  float(x) / float(z)
        print(res)