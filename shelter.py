##########
# Vars
##########

math = '0123456789+-/*()'
Vars = {}
Vars['0x0000'] = None
Error = {
    1: "Error with Compiling. Code is not supported.",
    2: "Error with Compiling. Variable wasn't placed.",
    3: "Error with Variable Grabbing. Variable was never set or not properly called.",
    4: "Error with Compiling. Invalid Input."
}

def error(errorcode):
    return ('\033[91m' + Error[errorcode] + '\033[0m')
def calc(input):
    input = input.replace('math{', '')
    input = input.replace('}', '')
    return input
def mathematics(cs, i):
    tex = ''
    State = 0
    resulttext = ''
    for char in cs:
        tex += char

        if tex == "{":
            tex = ''
            State = 1

        if tex == "}":
            tex = ''
            State = 0

        if State == 0:
            tex = ''

        if State == 1:
            if tex in math or tex == " ":
                resulttext += tex
            else:
                return "NOT POSSIBLE"
            tex = ''

    if State == 1:
        value = cs.split()
        return value[i]

    elif State == 0:
        cs = cs.replace(resulttext, str(float(eval(resulttext))))
        return cs

def ifstates(commands):
    result = []
    for command in commands:
        result.append(Lexer(command))
        continue
    return result


def Lexer(text):

    if text[0] == "?":
        return None

    value = text.split()
    i = -1
    for x in value:
        i = i + 1
        if 'var.' in x:
            if x[0:4] == "var.":
                if Vars.get(x[4:len(x)+1]) != None:
                    value[i] = Vars.get(x[4:len(x)+1])
                else:
                    return (error(3))
        if 'math{' in x:
            if x[0:5] == "math{" or x[0:5] == "Math{":
                    ttext = mathematics(text, i)
                    if ttext != "NOT POSSIBLE":
                        value = ttext.split()
                        value[i] = calc(value[i])


    if len(value) > 1:
        if value[1].lower() == "said:":
            if len(value) > 2:
                return (' '.join(value[2:len(value) + 1]))
            else:
                return (error(4))

        if value[1].lower() == "remembered:":
            if value[1] == value[-1]:
                return (error(2))

            if len(value) > 3:
                if value[3] == "=" and value[-1] != "=":
                    Vars[value[2]] = ' '.join(value[4:len(value) + 1])
                    return ("Memorized " + value[2] + " as " + Vars[value[2]])

                else:
                    return("Error. Inappropriate code.")

            else:
                Vars[value[2]] = None
                return ("Memorized " + value[2])

        if value[1].lower() == "left":
            return ("You'd fit perfectly to me and we'd end our loneliness.")

        if value[1].lower() == "checked":
            if len(value) > 5:
                if value[2].lower() == "if:":
                    if value[3] != None and value[5] != None:
                        if value[4] != None:
                                listcommands = []
                                while True:
                                    ifexe = input('>>>')
                                    if ifexe != "":
                                        if (len(ifexe) - len(ifexe.lstrip()) > (len(text) - len(text.lstrip()))):
                                            listcommands.append(ifexe)
                                            continue
                                        else:
                                            return 'Inappropriate Indentation.'
                                    else:
                                        if value[4] == "==":
                                            if value[3] == value[5]:
                                                x = ifstates(listcommands)
                                                for output in x:
                                                    if output == None:
                                                        continue
                                                    else:
                                                        print(output)
                                            return None

                                        if value[4] == "!=":
                                            if value[3] != value[5]:
                                                x = ifstates(listcommands)
                                                for output in x:
                                                    if output == None:
                                                        continue
                                                    else:
                                                        print(output)
                                            return None
                        else:
                            return "Use '==' in checked command"

                    else:
                        return 'CALL A VARIABLE ERROR!'


            else:
                return 'Error here.'


        else:
            return(error(1))
    else:
        return (error(1))

def run(text):
    lexer = Lexer(text)
    return lexer