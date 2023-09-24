def cleanComments(codeText: str) -> str:
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
    return uncommentedCodeText
