import scanner
import _token as tkn
scanner = scanner.scanner("test.aa")


Tokens = {
    "(" : tkn._Token_("LAPAREN","SPC_CHARECTER"),
    ")" : tkn._Token_("RPAREN","SPC_CHARECTER"),
    '"'  : tkn._Token_("STR_SIGN","SPC_CHARECTER"),
    ';' : "ENDLINE",
    "print" : tkn._Token_("PRINT","FUNC")
    }


for lineNo in range(scanner.getTotalLinesInFile()):
    pass