def generate_hollow_inverted_right_angled_triangle(n):
    result = []
    
    for i in range(n, 0, -1):
        if i == n:
            # Top row (full)
            result.append("*" * n)
        elif i == 1:
            # Bottom row (single star)
            result.append("*")
        else:
            # Hollow rows
            row = "*" + " " * (i - 2) + "*"
            result.append(row)
    
    return result
print(generate_hollow_inverted_right_angled_triangle(5))