def generate_sandglass(n):
    result = []
    
    # Top half (including middle)
    for i in range(n):
        spaces = " " * i
        stars = "*" * (2 * (n - i) - 1)
        result.append(spaces + stars + spaces)
    
    # Bottom half
    for i in range(n - 2, -1, -1):
        spaces = " " * i
        stars = "*" * (2 * (n - i) - 1)
        result.append(spaces + stars + spaces)
    
    return result
print(generate_sandglass(5))