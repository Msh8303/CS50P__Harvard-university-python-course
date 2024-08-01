input_ = input ("File name: ")
input_ = input_.lower().strip()
splitted = input_.split('.')
image_ = ["gif" ,"jpg", "jpeg", "png"]
application_ = ["pdf",  "zip"]
if splitted[-1] == 'jpg':
    splitted[-1] = 'jpeg'
if splitted[-1]  in image_:
    print(f'image/{splitted[-1]}')
elif splitted[-1] in application_:
    print(f'application/{splitted[-1]}')
elif splitted[-1] == "txt":
    print(f'text/{splitted[0]}')
else:
    print("application/octet-stream")