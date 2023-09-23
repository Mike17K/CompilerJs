import os

codeFile = open("code.txt", "r")
codeText = codeFile.read()


# remove all comments
mode = None # can be "//" or "/*"
adding = True
uncommentedCodeText = ""

i = 0
while(i<len(codeText)):
    letter = codeText[i]

    if letter == "/" and mode == None:
        if codeText[min(i+1,len(codeText)-1)] == "/":
            mode = "//"
        elif codeText[min(i+1,len(codeText)-1)] == "*":
            mode = "/*"
        adding = False
    elif letter == "\n" and mode == "//":
        adding = True
        mode = None
        
    elif letter == "*" and mode == "/*":
        if codeText[min(i+1,len(codeText)-1)] == "/":
            mode = None
            i += 2
            adding = True
    if adding:
        uncommentedCodeText += codeText[i]
    i += 1
codeText = uncommentedCodeText




symbols = ["'",'"','+', '-', '*', '/', '%', '^', '(', ')', '{', '}', '[', ']', ';', ':', ',', '.', '=', '<', '>', '!', '&', '|']
openingSymbols = ['(', '{', '[', '"', "'"]
closingSymbols = [')', '}', ']', '"', "'"]

openingClosingPairs = {
    "'": "'",
    '"': '"',
    '(': ')',
    '{': '}',
    '[': ']'
}
exmpectingSymbol = lambda x: openingClosingPairs[x] if x in openingSymbols else False

# opening closing symbols check
symbolStack = []

# command check
startIndex = None
endIndex = None
command = ""
includeSymbol = False

commands = [] 

for i in range(len(codeText)):
    letter = codeText[i]

    lastSymbol = symbolStack[-1] if len(symbolStack)!=0 else ""
    
    # command check
    if letter in symbols or letter in [" ", "\n", "\t"]: 
        endIndex = i
        if startIndex != None:
            includeSymbol = "'" in symbolStack or '"' in symbolStack and letter!=exmpectingSymbol(lastSymbol)
            if not includeSymbol:
                command = {"text":codeText[startIndex:endIndex]}
                startIndex = None
                endIndex = None

                command["type"] = "string" if "'" in symbolStack or '"' in symbolStack else "command"
                commands.append(command)
    else:
        if startIndex == None:
            startIndex = i
    

    # opening closing symbols check
    if exmpectingSymbol(lastSymbol) == letter:
        symbolStack.pop()
        # here we go up on the tree by one
    elif letter in openingSymbols or letter in closingSymbols:
        symbolStack.append(letter)
        # here we go down on the tree by one
    elif letter == ";" and ("'" not in symbolStack or '"' not in symbolStack):
        pass
        # end of line raimaining on the same tree level
        





isValid = True
isValid = isValid and len(symbolStack) == 0

print(commands)
print(isValid)