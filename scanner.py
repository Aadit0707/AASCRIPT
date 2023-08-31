import _token as tkn
import dictionary


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


        self.Tokens = dictionary.Tokens

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


        """
        #DEFINING ALL THE TOKENS
        

    def getNextChar(self):
        return self.charArray[self.currentChar+1]
    

    def advanceChar(self):
        self.currentChar +=1
        print(self.charArray[self.currentChar])
        return self.charArray[self.currentChar]
    
    def getTotalLinesInFile(self):
        return len(self.linesArray)

    def advanceLine(self):
        inString = False
        TokenArray = []
        line = ""
        string = ""
        stringDeclaredNow = False

        if ((len(self.linesArray)-1-1) >= self.currentLine):# -1 for starting by default at (-1) and -1 again because arrays start at 0
            self.currentLine += 1
            self.charArray = list(self.linesArray[self.currentLine])
            #print(self.charArray)
        else:
            print("ERROR: TRYING TO EXECUTE A LINE THAT DOES NOT EXIST")
        

        for newCharecter in self.charArray:
            
            line = line+newCharecter
            
            #add the newCharecter to the string
            if inString :
                
                #adds string
                """#print(newCharecter)"""
                string = string + newCharecter
            
            for x in self.Tokens: # checks if any token matches
                #done first


                
                if line == x :
                    #print(line)
                
                    TokenArray.append(self.Tokens.get(x)) #get the token that matched an append it


                if newCharecter == x:
                    
                    
                    if newCharecter == '"' and inString == False: 
                        inString = True
                        
                    elif newCharecter == '"' and inString == True : 
                        string= string[:-1] # removes the last and excess ' " ' charecter
                        inString = False
                        TokenArray.append(tkn._Token_("STRING_VAL","VALUE",_value = string)) # added the string to array
                        string = "" #resets string for reuse
                    elif newCharecter != '"' and inString == False:
                        TokenArray.append(self.Tokens.get(x))
                
                    
                """ print(line) """
        
        """
        for n in TokenArray:
            n.printToken()
        """
        
        return TokenArray
