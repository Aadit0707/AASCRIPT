
dictionary = {
    "print" : "PRINT",
    "(" : "BRACKET_START",
    ")" : "BRACKET_CLOSE",
    '"'  : "STR",
    ';' : "ENDLINE"
}


codePath = input("Code Path : ")
codecPath = codePath+"x"


code = open(codePath,"r")
codec  = open(codecPath,"w")
inString = False

compiledCode = []
for x in code:
    lineArray = list((x.lower()))
    
    print(lineArray)
    print(lineArray[1])

    lineArrayStriped = list((x.lower()))
    line = ""
    for newCharecter in lineArrayStriped:
        line = line+newCharecter
        StrCurrentLine = False
        if line == "print" and inString == False:
            compiledCode.append(dictionary["print"])
            compiledCode.append("\n")

        


        if newCharecter == '"' and inString == True and StrCurrentLine == False:
            print("start")
            compiledCode.append("\n") 
            compiledCode.append(dictionary['"']+"END")
            compiledCode.append("\n")
            inString = False
            StrCurrentLine = True
        
        if newCharecter == '"' and inString == False and StrCurrentLine == False:
            compiledCode.append(dictionary['"']+"START")
            compiledCode.append("\n")
            inString = True
            StrCurrentLine = True

        if inString == True and StrCurrentLine == False:
            print(line)
            compiledCode.append(newCharecter) 
         
        if newCharecter == "(" and inString == False:
            compiledCode.append(dictionary["("])
            compiledCode.append("\n") 

        if newCharecter == ")" and inString == False:
            compiledCode.append(dictionary[")"])
            compiledCode.append("\n")
        
        if newCharecter == ";" and inString == False:
            compiledCode.append(dictionary[";"])
            compiledCode.append("\n")



    """
    if lineArray[:5] == list("print"):
        compiledCode.append(dictionary["print"])
        compiledCode.append("\n")
        if lineArray[5] == "(":
            compiledCode.append(dictionary["("])
            compiledCode.append("\n")
    """

    

codec.writelines(compiledCode)
