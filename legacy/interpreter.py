dictionary = {
    "print" : "PRINT\n",
    "(" : "BRACKET_START\n",
    ")" : "BRACKET_CLOSE\n",
    "strStart" : "STRSTART",
    "strEnd" : "STREND",
    ';' : "ENDLINE"
}


path = input("path please : ")

codec = open(path,"r")
inStr = False
lno = 0

for line in codec:
    lno += 1
    codecLines=  codec.readlines()
    if line == dictionary["print"]:
        print("S")
        print(codecLines[lno])
codec.close()