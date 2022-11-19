import shelter

while True:
    text = input('basic > ')
    if text != "":
        result = shelter.run(text)
        print(result)