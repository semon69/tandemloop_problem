def calculator(a, b, s):
    if(s == '+'):
        return a + b
    if(s == '*'):
        return a * b
    if(s == '-'):
        return a - b
    if(s == '/'):
        return a / b
    
a = float(input())
b = float(input())
s = str(input())

print(calculator(a, b, s))