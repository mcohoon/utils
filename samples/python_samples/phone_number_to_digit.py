def phoneNumberToDigits(phoneNumbWithLetters):

    LetterValues = {
        'A': 2, 'B': 2, 'C': 2, 'D': 3, 'E': 3, 'F': 3, 'G': 4, 'H': 4, 'I': 4, 'J': 5, 'K': 5, 
        'L': 5, 'M': 6, 'N': 6, 'O': 6, 'P': 7, 'Q': 7, 'R': 7, 'S': 7, 'T': 8, 'U': 8, 'V': 8, 
        'W': 9, 'X': 9, 'Y': 9, 'Z': 9
        }

    phoneUpperCaseLetters = ""
    phoneNumeric = ""

    # error check input: make all characters upper case
    for i in phoneNumbWithLetters:
        c = str(i)
        if c.islower():
            uppercase = c.upper()
            phoneUpperCaseLetters += uppercase
        elif c.isupper():
            phoneUpperCaseLetters += c
        elif c is "-":
            pass
        elif c.isdigit():
            phoneUpperCaseLetters += c
        else:
            return str(c) + " is not a valid character"
    #print phoneUpperCaseLetters

    #
    for n in range(len(phoneUpperCaseLetters)):
        x = str(phoneUpperCaseLetters[n])
        if x.isdigit():
            phoneNumeric += x
        elif x.isalpha():
            numbValue = LetterValues[x]
            phoneNumeric += str(numbValue)

    return phoneNumeric

print "1-800-COM-CAST"
print phoneNumberToDigits('1-800-COM-CAST')
print "1-800-flo-WERS"
print phoneNumberToDigits('1-800-flo-WERS')
print "1-800-?ma-W[\RS"
print phoneNumberToDigits('1-800-?ma-W[\RS')
