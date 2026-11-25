def main():
    input_string = input("What the string you want to have as making faces: ")
    print(convert(input_string))

def convert(input_string):
    output_string = input_string.replace(":)", "🙂").replace(":(", "🙁")
    return output_string

main()