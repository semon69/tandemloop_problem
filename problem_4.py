def countMultiples(numbers):
    counts = {i: 0 for i in range(1, 10)}
    
    for i in range(1, 10):
        count = sum(1 for num in numbers if num % i == 0)
        counts[i] = count
    return counts

print(countMultiples([1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]))    