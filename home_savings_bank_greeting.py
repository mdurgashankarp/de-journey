greeting_input = input("Greeting: ")

if 'hello' in greeting_input.lower().strip() :
    print('$0')
elif greeting_input.lower().strip().startswith('h') and 'hello' not in greeting_input.lower().strip():
    print('$20')
else:
    print('$100')