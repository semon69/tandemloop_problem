def oddNumber(a):
    numbers= []
    for i in range(1, a+1):
        numbers.append((2*i) -1)
    return numbers 

a = int(input())

print(oddNumber(a))