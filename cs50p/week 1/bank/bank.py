input_ = input ("Greeting: ")
input_ = input_.lower()
splited = input_.split()

if splited[0] == 'hello' or input_.startswith('hello'):
    print("$0")
elif input_.startswith("h"):
    print("$20")
else:
    print("$100")