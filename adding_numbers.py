inp1 = input("num1: ")
inp2 = input("num2: ")

def add(number1, number2):
    i = 0
    if((inp1 and inp2) <= '9')  and ((inp1 and inp2) >= '0'):
        i = 1
    if i == 0:
        return "Invalid Input"
    number1 = int(number1)
    number2 = int(number2)

    return number1 + number2
print(str(add(inp1, inp2)))



