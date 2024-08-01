
input_ = input()
def convert(input_):
    emoji_dict = {':(' : "🙁", ':)' : "🙂"}

    for emotion, emoji in emoji_dict.items():
        input_ = input_.replace(emotion, emoji)
       
    return input_

result = convert(input_)
print(result)