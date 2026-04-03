def generate_number_pyramid(n):
    result = []
    
    for i in range(1, n + 1):
        # Create numbers like "1 2 3"
        numbers = " ".join(str(j) for j in range(1, i + 1))
        
        # Center the row with total width = 2*n - 1
        row = numbers.center(2 * n - 1, " ")
        
        result.append(row)
    
    return result
print(generate_number_pyramid(6))