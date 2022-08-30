inp1 = str(input("num1: "))
inp2 = str(input("num2: "))
  #receive input string vals
def add(number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    #convert to int
    return number1 + number2
  #add
result = add(inp1, inp2)
result = str(result)
  #back to int then print
print(result)


