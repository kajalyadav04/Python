ch=input()[0]
# print(ch)
def printAscii( ch):
        # ascii = ch.encode()[0]
        for i in range(256):
            if chr(i)==ch:
                ascii=i
        
        print(ascii)
def printAsciifn(ch):
         ascii = ch.encode()[0]
         print(ascii)
printAsciifn(ch)