def calculator(a, b, s):
    if(s == '+'):
        return a + b
    if(s == '*'):
        return a * b
    if(s == '-'):
        return a - b
    if(s == '/'):
        return a / b
    

print(calculator(3.45, 4.12, '+'))