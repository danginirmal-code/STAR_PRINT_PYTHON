def generate_diamond(n):
    result = []
    
    # Upper part (including middle row)
    for i in range(1, n + 1):
        stars = "*" * (2 * i - 1)
        row = stars.center(2 * n - 1)
        result.append(row)
    
    # Lower part (mirror of upper, excluding middle row)
    for i in range(n - 1, 0, -1):
        stars = "*" * (2 * i - 1)
        row = stars.center(2 * n - 1)
        result.append(row)
    
    return result

print(generate_diamond(5))