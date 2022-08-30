inp1 = str(input("num1: "))
inp2 = str(input("num2: "))
x = 4
if((inp1 and inp2) <= '9')  and ((inp1 and inp2) >= '0'):
    x = 0
    
if x == 4:
    print("invalid input")
    exit()
def add(number1, number2):
    number1 = int(number1)
    number2 = int(number2)

    return number1 + number2
result = add(inp1, inp2)
result = str(result)
print(result)


