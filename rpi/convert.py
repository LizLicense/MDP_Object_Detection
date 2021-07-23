import sys

def hexDec(s):
    #s = '0xc8' - 12
    print(int(s,16))
#    return int(s,16)
def decHex(d):
    print(hex(int(d)))
#    return hex(d)

def main():
    #print('a')
    s = sys.argv[1]
    if s.isnumeric():
        decHex(s)
    else:
        hexDec(s)    
    #print(sys.argv[1])
if __name__ == "__main__":
    main()
    #for i , arg in enumerate(sys.argv):
    #print(sys.argv[1])

#hexDec('0xc8')
#decHex(200)
