from math import pow
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ." #35

class Number:
    def __init__(self,valueString,base = 10, numericList = []):   #Formats: 'numeric, 'alphanumeric'
        self.digits = []
        self.base = base
        if valueString != "ignore":
            try:
                for v in valueString:
                    self.digits.append(DIGITS.find(v))
            except:
                print('Something went wrong. Make sure base is less than 35.')
        else:
            self.digits = numericList

    def value(self, format = "alphanumeric"):
        valueStr = ""
        try:
            for index in self.digits:
                valueStr += DIGITS[index]
        except:
            print("Cannot format a number with base greater than 35.")
        return valueStr
    
    def __add__(self,n2):
        result = []
        if self > n2:
            result = [0]* (len(self.digits) + 1)
        else:
            result = [0]* (len(n2.digits) + 1)
        
        selfDigits = [0]*len(result)
        for i in range(len(self.digits)):
            selfDigits[len(selfDigits)-1-i] = self.digits[len(self.digits)-1-i]
        n2Digits = [0]*len(result)
        for i in range(len(n2.digits)):
            n2Digits[len(n2Digits)-1-i] = n2.digits[len(n2.digits)-1-i]

        c=0
        s=0
        for i in range(len(result) - 1):
            totalSum = (selfDigits[len(selfDigits) - i - 1] + n2Digits[len(n2Digits) - i - 1]) + c
            s = totalSum % self.base
            c = totalSum // self.base
            result[len(result) - 1 - i] = s
        if c != 0:
            result[0] = c
        else:
            result.pop(0)

        return Number("ignore",self.base,result)

    def __gt__(self,n2):
        if len(self.digits) > len(n2.digits) and self.base == n2.base:
            return True
        elif len(self.digits) == len(n2.digits):
            for i in range(len(self.digits)):
                if self.digits[i] > n2.digits[i]:
                    return True
                elif self.digits[i] == n2.digits[i]:
                    pass
                else:
                    return False
            return False
        else:
            return False

    def decimalValue(self):
        sum = 0
        for i in range(len(self.digits)):
            sum += int(self.digits[i]*(pow(self.base,len(self.digits) - 1 - i)))
        return sum

    def numberTobase(self, base2):
        qStack = [] #Stack for Q

        Qprev = self.decimalValue()
        print("d: ", Qprev)
        Qcur = 0
        R = 0

        while Qprev != 0:
            Qcur = Qprev//base2
            R = Qprev%base2
            qStack.append(R)
            Qprev = Qcur

        tempL = []
        for i in range(len(qStack)):
            tempL.append(qStack.pop())
        self.digits = tempL
        self.base = base2

n1 = Number("23", 10)
n2 = Number("26", 10)

print (n1 > n2)
print (n2 > n1)
print(n1.value())
print(n2.value())

print()
n3 = n1 + n2
print(n3.value())

print(n1.decimalValue())
print(n2.decimalValue())

print(n1.value())
n1.numberTobase(2)
print(n1.value())

def numberToBase(n,base1,base2):
    qStack = [] #Stack for Q

    Qprev = n
    Qcur = 0
    R = 0

    while Qprev != 0:
        Qcur = Qprev/base2
        R = Qprev/base2
        qStack.append(R)
        Qprev = Qcur
    


