
dictionary = {
    "print" : "PRINT\n",
    "(" : "BRACKET_START\n",
    ")" : "BRACKET_CLOSE\n",
    '"'  : "STR\n",
    ';' : "ENDLINE\n"
}


codePath = input("Code Path : ")
codecPath = codePath+"x"


code = open(codePath,"r")
codec  = open(codecPath,"w")
inString = False

compiledCode = []
for x in code:
    lineArray = list((x.lower()))
    

    lineArrayStriped = list((x.lower()))
    line = ""
    currentFunc = ""
    lineToPrint = ""
    for newCharecter in lineArrayStriped:
        
        line = line+newCharecter
        StrCurrentLine = False
        
        if line == "print" and inString == False:
            compiledCode.append(dictionary["print"])
            compiledCode.append("\n")
            currentFunc = dictionary["print"]
        if currentFunc == dictionary["print"] and newCharecter == "(":
            pass
        else:
            pass
        if currentFunc == dictionary["print"] and newCharecter ==  '"' and inString == False:
            inString = True
            StrCurrentLine = True
        elif currentFunc == dictionary["print"] and newCharecter ==  '"' and inString == True:
            inString = False
            
        if inString == True and StrCurrentLine == False:
            lineToPrint = lineToPrint+newCharecter
            
        if newCharecter == ")" and currentFunc == dictionary["print"]:
            print(lineToPrint)
        

        """
        if newCharecter == '"' and inString == True and StrCurrentLine == False:
            #print("start")
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
            #print(line)
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

    """
    if lineArray[:5] == list("print"):
        compiledCode.append(dictionary["print"])
        compiledCode.append("\n")
        if lineArray[5] == "(":
            compiledCode.append(dictionary["("])
            compiledCode.append("\n")
    """


codec.writelines(compiledCode)
codec.close()
code.close()