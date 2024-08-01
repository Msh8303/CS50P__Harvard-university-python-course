print("Amount Due: 50")
due = 50


while due != 0:
    input_ = int(input("Insert Coin: "))
    if input_ <= due:

        if (input_ == 5) or (input_ == 10) or (input_ == 25):
            due -= input_
            print(f'Change Owed: {due}')    if (due == 0) else print(f'Amount Due: {due}')


        else:
            print(f'Amount Due: {due}')
            continue
    else:
        print(f'Change Owed: {input_ - due}')
        break