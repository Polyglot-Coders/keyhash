import random

__author__ = 'Spartan'

library = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' \
    ,'!','@','#','$','%','^','&','*','(',')','-','_','=','+','[','{',']','}', 'A','B','C','D','E','F','G','H','I','J', \
           'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']


class Crypto () :

    def __init__(self):
        self.sitekey = ""


    def setSiteKey (self) :
        self.sitekey = self.keyGen(128)
        return self.sitekey


    def keyGen (self, length) :
        keyString = ''
        for i in range(0, length):
            ranNum = random.randint(0, len(library) - 1 )
            keyString += library[ranNum]

        return keyString

    def scramble (self, key):

        siteArr = list(self.sitekey)
        deckA = []
        deckB = []
        returnedKey = []
        key = list(key)

        for k in range(0, len(key)):
            returnedKey.append(library.index(key[k]))

        for i in range(0, 7):
            for a in range(0, len(siteArr)):
                index = library.index(siteArr[a])

                if (index % 2 == 0):
                    deckA.append(returnedKey[a])
                else :
                    deckB.append(returnedKey[a])

            returnedKey = []

            for a in range(0, len(deckB)):
                returnedKey.append(deckB[a])

            for a in range(0, len(deckA)):
                returnedKey.append(deckA[a])

            deckA = []
            deckB = []

        hashed = ""
        for i in range(0, len(returnedKey)):
            hashed += library[returnedKey[i]]

        return hashed

    def unscramble (self, hash):
        key = ""
        deckA = []
        deckB = []
        siteArr = list(self.sitekey)
        keyArr = list(hash)
        deckALength = 0
        deckBLength = 0

        for s in range(0, len(siteArr)):
            index = library.index(siteArr[s])

            if index % 2 == 0:
                deckALength+=1
            else :
                deckBLength+=1

        for i in range(0, 7):
            for b in range(0, deckBLength):
                deckB.append(keyArr[b])
            for a in range(deckBLength, len(keyArr)):
                deckA.append(keyArr[a])

            keyArr = []
            deckAinc = 0
            deckBinc = 0

            for s in range(0, len(siteArr)):
                index = library.index(siteArr[s])
                if (index % 2 == 0):
                    keyArr.append(deckA[deckAinc])
                    deckAinc += 1
                else :
                    keyArr.append(deckB[deckBinc])
                    deckBinc+=1
            deckA = []
            deckB = []

        for i in range(0, len(keyArr)):
            key += keyArr[i]

        return key


test = Crypto()
test.setSiteKey()

newKey = test.keyGen(128)
scramble = test.scramble(newKey)

unscramble = test.unscramble(scramble)
print unscramble == newKey