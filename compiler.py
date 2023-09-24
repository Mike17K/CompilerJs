from helpers.comment_cleaner import cleanComments
import os

codeFile = open("code.txt", "r")
codeText = codeFile.read()

codeText = cleanComments(codeText)



symbols = ["'",'"',"`",'+', '-', '*', '/', '%', '^', '(', ')', '{', '}', '[', ']', ';', ':', ',', '.', '=', '<', '>', '!', '&', '|']
openingSymbols = ['(', '{', '[', '"', "'","`"]
closingSymbols = [')', '}', ']', '"', "'","`"]

types = ["let","var"]

openingClosingPairs = {
    "`":"`",
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
    lastCommand = commands[-1] if len(commands)!=0 else {"text":"", "type":"None"}
    # command check
    if letter in symbols or letter in [" ", "\n", "\t"]: 
        endIndex = i
        if startIndex != None:
            includeSymbol = "'" in symbolStack or '"' in symbolStack and letter!=exmpectingSymbol(lastSymbol)
            if not includeSymbol:
                command = {"text":codeText[startIndex:endIndex]}
                startIndex = None
                endIndex = None

                if "'" in symbolStack or '"' in symbolStack: 
                    command["type"] = "string" 
                elif command['text'] in types:
                    command['type'] = "type"
                elif lastCommand['type'] == "type":
                    command['type'] = 'variable'
                else:
                    command['type'] = "unknown" # TODO FIX

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


for c in commands:
    print(c)

print(isValid)