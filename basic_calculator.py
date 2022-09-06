n1 = int(input("enter num1: "))
n2 = int(input("enter num2: "))
Uop = input("enter op: ")
def calc(n1, n2, op):
    if op == '+':
        end = n1 + n2    
    elif op == '-':
        end = n1 - n2
    elif op == '/':
        if n1 == 0 or n2 == 0:
            end = "cat divide by 0" 
        else:
            ebd = n1 / n2    
    elif  op == '*':
        end = n1*n2
    else:
        end = "enter a proper op either[+, -, *, /]"
    return end
print(calc(n1, n2, Uop))
