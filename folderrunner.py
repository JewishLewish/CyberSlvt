import shelter

for command in open('main.svlt', 'r').readlines():
    if command == '\n':
        continue
    else:
        result = shelter.run(command)
        if result == None:
            continue
        elif result == "You'd fit perfectly to me and we'd end our loneliness.":
            print(result)
            exit(0)
        else:
            print(result)