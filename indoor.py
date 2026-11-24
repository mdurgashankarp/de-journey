def main():
    inputString = input("What is the string you want to convert to lower case: ")
    print("The output string after coverting to lower case is:", changeTheStringToLowerCase(inputString))

def changeTheStringToLowerCase(inputString):
    outputString = inputString.lower()
    return outputString

main()