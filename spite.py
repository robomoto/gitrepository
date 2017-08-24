##Usage: 
##  >>encode('your secret message here')
##  >>File: path/to/key.txt
##
##  >>decode('1 2 3 4 5')
##  >>File: path/to/key.txt
##=================

def loadCode():
      ## Read in the key file
    src = raw_input('File: ')
    with open (src, "r") as code:
        data=tuple(code.read().lower())
    return data

def encode(message):
  ## encode takes the encoding data file and message and outputs a string of numbers
    data=loadCode()
    message = message.lower()
    counter = 0
    currentIndex = 0
    i=0
    lenMsg = len(message)
    lenData = len(data)-1
    val = ''
    while i < lenMsg:
        b = False
        while b == False:
            if message[i] == data[currentIndex]:
                val+=str(counter)+' '
                counter = 0;
                b = True;
            else:
                currentIndex += 1
                counter += 1
                if currentIndex == lenData:
                    currentIndex = 0
                if counter == lenData:
                    val+= '-1 '
                    counter = 0
                    b = True
            if currentIndex == lenData:
                currentIndex = 0
        i += 1;
    return val

def decode(code):
  ## decode takes the encoding data file and string of numbers and returns the original string
    data=loadCode()
    code = [int(i) for i in code.split()]
    dataIndex = 0
    codeIndex = 0
    codeLength = len(code)
    dataLength = len(data) - 1
    val = ''
    while codeIndex < codeLength:
        if code[codeIndex] == -1:
            val+='#'
        else:
            dataIndex += code[codeIndex]
            if dataIndex > dataLength:
                dataIndex -= dataLength
            val += data[dataIndex]
        codeIndex += 1
    print val  
