def main():
    print("I am inside main, next step is to run hello!")
    x = int(input("X: "))
    y = int(input("Y: "))
    print(f"the function gives me", hello(x,y))

def hello(x,y):
    print("calculate what is x/y?") 
    return float(x/y)

main()



""" print("Hello, Shankar!", end = '')
name = input("What is your name?")
print(f"My name is {name}") """

