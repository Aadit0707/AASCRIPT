import _token as tkn

class scanner:
    def __init__(self,_file):
        self.file = open(_file,"r")
        self.linesArray = self.file.readlines()
        self.currentLine = -1
        self.currentChar = -1
        self.charArray = []


        """
        self.specialCharecters = {
            "(" : "LAPAREN",
            ")" : "RPAREN",
            '"'  : "STR",
            ';' : "ENDLINE"
        }
        self.funcs = {
                "print" : "PRINT"
                }
        """


        self.Tokens = {
            "(" : tkn._Token_("LAPAREN","SPC_CHARECTER"),
            ")" : tkn._Token_("RPAREN","SPC_CHARECTER"),
            '"'  : tkn._Token_("STR","SPC_CHARECTER"),
            ';' : "ENDLINE",
            "print" : tkn._Token_("PRINT","FUNC")
        }
        #DEFINING ALL THE TOKENS

    def getNextChar(self):
        return self.charArray[self.currentChar+1]
    def advanceChar(self):
        self.currentChar +=1
        print(self.charArray[self.currentChar])
        return self.charArray[self.currentChar]
    def advanceLine(self):
        inString = False
        TokenArray = []


        if ((len(self.linesArray)-1-1) >= self.currentLine):# -1 for starting by default at (-1) and -1 again because arrays start at 0
            self.currentLine += 1
            self.charArray = list(self.linesArray[self.currentLine])
            print(self.charArray)
        else:
            print("ERROR: TRYING TO EXECUTE A LINE THAT DOES NOT EXIST")
        

        line = ""

        for newCharecter in self.charArray:
            line = line+newCharecter

            for x in self.Tokens: # checks if any token matches

                if line == x :
                    print(line)
                    TokenArray.append(self.Tokens.get(x)) #get the token that matched an append it
                
                if newCharecter == x:
                    
                    TokenArray.append(self.Tokens.get(x))
                print(line)
            
        for n in TokenArray:
            n.printToken()