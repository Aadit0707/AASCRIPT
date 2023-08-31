import scanner
import dictionary
import _token as tkn
scanner = scanner.scanner("test.aa")

"""
The _Token_ class has 3 variables :
    value(optional)
    type eg : SPC_CHARECTER,FUNC
    name eg  : RPAREN,PRINT
"""

Tokens = dictionary.Tokens

# this is what dictionary.Tokens looks like (yet)
"""

Tokens = { 
    "(" : tkn._Token_("LAPAREN","SPC_CHARECTER"),
    ")" : tkn._Token_("RPAREN","SPC_CHARECTER"),
    '"'  : tkn._Token_("STR_SIGN","SPC_CHARECTER"),
    ';' : "ENDLINE",
    "print" : tkn._Token_("PRINT","PREFUNC"),
    "if" : tkn._Token_("IF","KEYWORD")
    }


Token Name : PRINT
Token Type : PREFUNC
Token Name : LAPAREN
Token Type : SPC_CHARECTER
Token Name : STRING_VAL
Token Type : VALUE
Token Value : Hello World
Token Name : RPAREN
Token Type : SPC_CHARECTER
"""


for lineNo in range(scanner.getTotalLinesInFile()):
    TokenArray = scanner.advanceLine()
    TokenArrayLen = len(TokenArray)
    currentFunc= None
    currentString = None
    for TokenNo in range(TokenArrayLen):
        match TokenArray[TokenNo].type:
        


            case "PREFUNC":
                match TokenArray[TokenNo].name:
                    case "PRINT":
                        if TokenArray[TokenNo+1] == Tokens["("]: # this may kinda seem confusing but it just checks if the object's parameters match an alternative can be if TokenArray[TokenNo+1].name == Tokens["("].name: 
                            currentFunc = TokenArray[TokenNo].name
                        else:
                            print("unrecognized text did you mean the function print?, if so then you forgot to add '(' after print ")
                            tkn.printTokenArray(TokenArray)
             
            

            case "SPC_CHARECTER":
                match TokenArray[TokenNo].name:
                    case "LAPAREN":
                        if TokenArray[TokenNo-1].type == "PREFUNC" or TokenArray[TokenNo-1].type == "KEYWORD":
                            pass
                    
                    case "RPAREN":
                        if currentFunc != None:
                            if currentFunc == Tokens.get("print").name and currentString != None:
                                print(currentString)
                                currentFunc = None
                                currentString = None
                            elif currentString == None and currentFunc == Tokens.get("print").name:
                                print("ERROR")
                                tkn.printTokenArray(TokenArray)

            case "VALUE":
                match TokenArray[TokenNo].name:
                    case "STRING_VAL":
                        if TokenArray[TokenNo].value != None:
                            currentString = TokenArray[TokenNo].value
                        else:
                            print("FAILED : STRING VALUE = NONE")


    if currentFunc != None:
        print("ERROR FAILED TO CLOSE FUNCTION, DID YOU FORGET ')' ? ")
