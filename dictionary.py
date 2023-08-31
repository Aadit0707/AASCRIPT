import _token as tkn


Tokens = { 
    "(" : tkn._Token_("LAPAREN","SPC_CHARECTER"),
    ")" : tkn._Token_("RPAREN","SPC_CHARECTER"),
    '"'  : tkn._Token_("STR_SIGN","SPC_CHARECTER"),
    ';' : "ENDLINE",
    "print" : tkn._Token_("PRINT","PREFUNC"),
    "if" : tkn._Token_("IF","KEYWORD")
    }
