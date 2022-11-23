##########
# Vars
##########

math = '0123456789+-/*()'
Varsil = '})]'
Vars = {}
Vars['0x0000'] = None
Vars['0x0001'] = 0
Vars['x'] = '2'
Error = {
    1: "Error with Compiling. Code is not supported.",
    2: "Error with Compiling. Variable wasn't placed.",
    3: "Error with Variable Grabbing. Variable was never set or not properly called.",
    4: "Error with Compiling. Invalid Input."
}
def variable(input):
    State = 0
    tex = ''
    result = ''
    replace = ''
    for char in input:
        tex += char
        if char in Varsil:
            continue

        if State == 0:
            if tex in 'var.':
                if tex == 'var.':
                    State = 1
                    replace += tex
                    tex = ''
            else:
                tex = ''

        if State == 1:
            if tex != ' ' or tex != '}':
                result += tex
                replace += tex
            else:
                tex = ''

    return(input.replace(replace, Vars[result]))

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
    rtext = ''

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
            rtext += tex

            if tex in math:
                resulttext += tex

            else:
                tex = ''
                continue

            tex = ''

    if State == 1:
        value = cs.split()
        return value[i]

    elif State == 0:
        cs = cs.replace(rtext, str(int(eval(resulttext))))
        return cs

def ifstates(commands):
    result = []
    for command in commands:
        result.append(Lexer(command))
        continue
    return result


def Lexer(text):

    if text[0] == "?": #Cancels The Code
        return None

    value = text.split()

    i = -1
    for x in value:
        i = i + 1
        if 'var.' in x:
            value[i] = variable(value[i])
            text = ' '.join(value)

    i = -1
    for x in value:
        if 'math{' in x:
            if x[0:5] == "math{" or x[0:5] == "Math{":
                    text = mathematics(text, i)
                    if text != "NOT POSSIBLE":
                        value = text.split()
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
                    return None

                else:
                    return("Error. Inappropriate code.")

            else:
                Vars[value[2]] = None
                return None

        if value[1].lower() == "left":
            return ("You'd fit perfectly to me and we'd end our loneliness.")

        if value[1].lower() == "checked":
            if len(value) > 5:
                if value[2].lower() == "if:" or value[2].lower() == "while:":
                    if value[3] != None and value[5] != None:
                        #print(value[3] + " and " + value[5])
                        if value[4] != None:
                                listcommands = []
                                while Vars['0x0001'] == 0:
                                    ifexe = input('...')
                                    if ifexe != "":
                                        if (len(ifexe) - len(ifexe.lstrip()) > (len(text) - len(text.lstrip()))):
                                            listcommands.append(ifexe)
                                            continue
                                        else:
                                            return 'Inappropriate Indentation.'
                                    else:
                                        Vars['0x0001'] = 1

                                if value[4] == "==":
                                    if value[2].lower() == "if:":
                                        if value[3] == value[5]:
                                            x = ifstates(listcommands)
                                            for output in x:
                                                if output == None:
                                                    continue
                                                else:
                                                    print(output)
                                    elif value[2].lower() == "while:":
                                        while value[3] == value[5]:
                                            x = ifstates(listcommands)
                                            for output in x:
                                                if output == None:
                                                    continue
                                                else:
                                                    print(output)

                                if value[4] == "!=":
                                    if value[3] != value[5]:
                                        x = ifstates(listcommands)
                                        for output in x:
                                            if output == None:
                                                continue
                                            else:
                                                print(output)
                                    elif value[2].lower() == "while:":
                                        while value[3] != value[5]:
                                            x = ifstates(listcommands)
                                            for output in x:
                                                if output == None:
                                                    continue
                                                else:
                                                    print(output)
                                Vars['0x0001'] = 0
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