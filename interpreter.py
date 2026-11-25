expression = input("Expression: ")

if ' ' in expression:
    match expression.split(' ')[1]:
        case '+':
            print(f"{(int(expression.split(' ')[0]) + int(expression.split(' ')[2])):.1f}")
        case '-':
            print(f"{(int(expression.split(' ')[0]) - int(expression.split(' ')[2])):.1f}")
        case '/':
            print(f"{(int(expression.split(' ')[0]) / int(expression.split(' ')[2])):.1f}")
        case '*':
            print(f"{(int(expression.split(' ')[0]) * int(expression.split(' ')[2])):.1f}")
        case _:
            print("Provide a valide expression")
else:
    print("Provide a valide expression")