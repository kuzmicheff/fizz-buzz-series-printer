def validateUserInput(rawUserInput): 
    try: 
        validUserInput = int(rawUserInput)
    except: 
        print("Data must be entered as a whole positive number!")
        rawUserInput = input("Please enter a whole positive number: ")
        return(validateUserInput(rawUserInput))
    if validUserInput >= 0: 
        return(validUserInput)
    else: 
        print("Data must be entered as a whole positive number!")
        rawUserInput = input("Please enter a whole positive number: ")
        return(validateUserInput(rawUserInput))

def printFizzBuzz (rangeStart, rangeEnd, rangeStep, rangeDivider1, rangeDivider2): 
    rangeEnd = rangeEnd + 1
    for i in range(rangeStart, rangeEnd, rangeStep): 
        if i == 0: 
            print(i)
        elif i == (rangeEnd): 
            break
        elif i % (rangeDivider1 * rangeDivider2) == 0: 
            print("FizzBuzz")
        elif i % rangeDivider1 == 0: 
            print("Fizz")
        elif i % rangeDivider2 == 0: 
            print("Buzz")
        else: 
            print(i)

def main(): 
    print("FizzBuzz Range Printer")
    rangeStartInput = input("Enter the starting number of the FizzBuzz range: ")
    validRangeStart = validateUserInput(rangeStartInput)
    rangeEndInput = input("Enter the ending number of the FizzBuzz range: ")
    validRangeEnd = validateUserInput(rangeEndInput)
    rangeStepInput = input("Enter the step increment for the FizzBuzz range: ")
    validRangeStep = validateUserInput(rangeStepInput)
    rangeDivider1Input = input("Enter the first divider for the FizzBuzz range: ")
    validRangeDivider1 = validateUserInput(rangeDivider1Input)
    rangeDivider2Input = input("Enter the second divider for the FizzBuzz range: ")
    validRangeDivider2 = validateUserInput(rangeDivider2Input)
    printFizzBuzz(validRangeStart, validRangeEnd, validRangeStep, validRangeDivider1, validRangeDivider2)

main()