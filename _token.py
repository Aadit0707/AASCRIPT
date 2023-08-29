class _Token_:
    def __init__(self,_name,_type):
        self.name = _name
        self.type = _type
    def printToken(self):
        print( "Token Name : " + self.name )
        print( "Token Type : " + self.type )