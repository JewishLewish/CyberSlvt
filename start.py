import shelter

while True:
    text = input('>>>')

    if text != "":
        result = shelter.run(text)
        if result == None:
            continue
        elif result == "You'd fit perfectly to me and we'd end our loneliness.":
            print(result)
            exit(0)
        else:
            print("heh" + result)
