print("SIMPLE CALCULATOR")

numOpe = []
a = 1
n = int(input("enter number:"))
numOpe.append(n)

def checkOpe(s):
    if s != '=':
        numOpe.append(s)
        n1 = int(input("enter number:"))
        numOpe.append(n1)
        s1 = input("enter operation(+,-,*,/,=):")
        checkOpe(s1)
    
    elif s == '=':
        if len(numOpe) == 1:
            print("The final value is:", n)
        else:
            i=0
            while i < len(numOpe):
                if numOpe[i] == '/':
                    res = numOpe[i-1] / numOpe[i+1]
                    numOpe[i-1:i+2]=[res]
                    i -= 1 if i > 0 else 0
                else:
                    i += 1
    
            i=0
            while i < len(numOpe):
                if numOpe[i] == '*':
                    res = numOpe[i-1] * numOpe[i+1]
                    numOpe[i-1:i+2]=[res]
                    i -= 1 if i > 0 else 0
                else:
                    i += 1
    
            i=0
            while i < len(numOpe):
                if numOpe[i] == '-':
                    res = numOpe[i-1] - numOpe[i+1]
                    numOpe[i-1:i+2]=[res]
                    i -= 1 if i > 0 else 0
                else:
                    i += 1
    
            i=0
            while i < len(numOpe):
                if numOpe[i] == '+':
                    res = numOpe[i-1] + numOpe[i+1]
                    numOpe[i-1:i+2]=[res]
                    i -= 1 if i > 0 else 0
                else:
                    i += 1
            print("The final value is:", numOpe[0])

if a == 1:
    s = input("enter operation(+,-,*,/,=):")
    checkOpe(s)