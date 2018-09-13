def readVal(valType, requestMsg, errorMsg):
    while True:
        val = input(requestMsg+' ')
        try:
            return(valType(val)) #converts string to valType
        except ValueError:
            print(val, errorMsg)

val = readVal(int, 'Enter an integer:', 'is not an integer')
