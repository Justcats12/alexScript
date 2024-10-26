import sys

program_path = sys.argv[1]

########
# LINE #
########

# Read file lines
program_lines = []
with open(program_path, "r") as program_file:
    program_lines = [line.strip() for line in program_file.readlines()]

line_tracker = 0
var_keeper = {}

################
# HELP METHODS #
################

def makeVar(name, type, value : str):
    match type:
        case "INT":
            var_keeper[name] = int(value)
        case "STR":
            assert value.startswith("\"") and value.endswith("\""), "String must start and end with \""
            var_keeper[name] = value[1:-1]
        case "BOOL":
            if value == "TRUE":
                var_keeper[name] = True
            elif value == "FALSE":
                var_keeper[name] = False
            else:
                var_keeper[name] = None
        case _:
            var_keeper[name] = None

def replaceSpaces(text):
    oldText = text
    newtext = ""
    inBrackets = False
    for c in oldText:
        if c == "\"":
            inBrackets = not inBrackets
        
        if inBrackets and c == " ":
            newtext += "_"
        else:
            newtext += c
    
    return newtext


###############
# INTERPRETOR #
###############

def parseText(programText : str) -> str:
    replacedText = replaceSpaces(programText)
    #print(replacedText)

    parts = replacedText.split(" ")
    #print(parts)
    # fill in variables
    for i in range(len(parts)):
        part = parts[i]
        if part.startswith("@"):
            value = var_keeper[part[1:]]
            # value is integer
            if isinstance(value, int):
                parts[i] = str(value)
            elif isinstance(value, str):
                parts[i] = f"\"{replaceSpaces(value)}\"" 
            elif isinstance(value, bool):
                if value:
                    parts[i] = "TRUE"
                else:
                    parts[i] = "FALSE"
            else:
                parts[i] = "NULL"
        elif part == "NEXT":
            parts[i] = str(line_tracker + 2)
            #print(line_tracker)
        elif part == "PREV":
            parts[i] = str(line_tracker)

    #print(parts, 2)

    # check if boolean equation or not
    if len(parts) == 3:
        output = None
        if parts[1] == "==":
            output = (parts[0] == parts[2])
        elif parts[1] == "!=":
            output = (parts[0] != parts[2])
        elif parts[1] == ">":
            output = (parts[0] > parts[2])
        elif parts[1] == "<":
            output = (parts[0] < parts[2])
        
        if output != None:
            if output:
                return "TRUE"
            return "FALSE"
    
    return " ".join(parts)




while program_lines[line_tracker] != "END":
    # get current line
    unparsedLine : str= program_lines[line_tracker]
    # check for boolean
    parsedLine = ""
    if "(" in unparsedLine and ")" in unparsedLine:
        indexes = unparsedLine.index("("), unparsedLine.index(")")
        toParse = unparsedLine[indexes[0]+1:indexes[1]]
        parsed = parseText(toParse)

        parsedLine = unparsedLine.replace(unparsedLine[indexes[0]:indexes[1]+1], parsed)
    else:
        parsedLine = unparsedLine
    
    parts = parsedLine.split(" ")
    
    instruction = parts[0]
    match instruction:
        case "SET":
            datatype = parts[1]
            varName = parts[2]
            assert parts[3] == "=", "SET must have an equal sign (=)"
            value = parseText(" ".join(parts[4:]))

            makeVar(varName, datatype, value)
        case "IF":
            condition = parts[1]
            ifTrue = parseText(parts[2])
            assert parts[3] == "ELSE", "IF statement must have an ELSE"
            ifFalse = parseText(parts[4])
            if condition == "TRUE":
                line_tracker = int(ifTrue) -1
            else:
                line_tracker = int(ifFalse) -1
            continue
        case "PRINT":
            statement = parseText(" ".join(parts[1:])).replace("_", " ").replace("\"", "")
            print(statement)
        case "JUMP":
            destination = parseText(parts[1])
            line_tracker = int(destination) -1
            continue
        case "INPUT":
            datatype = parts[1]
            varName = parts[2]
            if datatype == "STR":
                value = parseText(f"\"{input()}\"")
            else:
                value = input()
            #print(value, line_tracker)
            makeVar(varName, datatype, value)
        case "SUM":
            varName = parts[1]
            allNumbers = [parseText(x) for x in parts[2:]]
            sumNumbers = str(sum([int(i) for i in allNumbers]))
            makeVar(varName, "INT", sumNumbers) 
        case _:
            line_tracker += 1
            continue
    
    line_tracker += 1

