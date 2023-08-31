class _Token_:
    def __init__(self,_name,_type,_value=None):
        self.name = _name
        self.type = _type
        self.value = _value
    def printToken(self):
        print( "Token Name : " + self.name )
        print( "Token Type : " + self.type )
        if self.value != None:
            print("Token Value : " + self.value)


def printTokenArray(TokenArray):
    for n in TokenArray:
        n.printToken()