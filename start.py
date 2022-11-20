import shelter

while True:
    text = input('basic > ')

    if text == "You'd fit perfectly to me and we'd end our loneliness.":
        exit(0)

    elif text != "":
        result = shelter.run(text)
        print(result)
