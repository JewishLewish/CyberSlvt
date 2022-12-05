import shelter2

while True:
    text = input('>>>')

    if text != "":
        result = shelter2.run(text)
        if result == None:
            continue
        elif result == "You'd fit perfectly to me and we'd end our loneliness.":
            print(result)
            exit(0)
        else:
            print(result)
