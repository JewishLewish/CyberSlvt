##########
# Vars
##########

math = '0123456789+-*/'
Vars = {}
Vars['0x0000'] = None

def calc(input):
    input = input.replace('math{', '')
    input = input.replace('}', '')
    return input

def mathematics(cs):
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
            resulttext += tex
            tex = ''
    cs = cs.replace(resulttext, str(eval(resulttext)))
    return cs

def Lexer(text):
    Out = ''

    if text[0] == "?":
        return None
        print('test')

    value = text.split()
    i = -1
    i2 = 0
    for x in value:
        i = i + 1
        if 'var.' in x:
            if x[0:4] == "var.":
                if Vars.get(x[4:len(x)+1]) != None:
                    value[i] = Vars.get(x[4:len(x)+1])
                else:
                    return ('Variable never was set.')
        if 'math{' in x:
            if x[0:5] == "math{":
                    text = mathematics(text)
                    value = text.split()
                    value[i] = calc(value[i])


    if len(value) > 1:
        if value[1] == "Said:":
            return (' '.join(value[2:len(value) + 1]))

        if value[1] == "Remembered:":
            Vars[value[2]] = None
            if len(value) > 3:
                if value[3] == "=" and value[-1] != "=":
                    Vars[value[2]] = ' '.join(value[4:len(value) + 1])
                    return ("Memorized " + value[2] + " as " + Vars[value[2]])


                else:
                    return("Error. Inappropriate code.")
            else:
                return("Error. Inappropriate code.")
        else:
            return("Error. Inappropriate code")



def run(text):
    lexer = Lexer(text)
    return lexer