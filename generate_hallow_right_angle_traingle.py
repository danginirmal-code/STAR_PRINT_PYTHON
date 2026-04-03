def generate_hollow_right_angled_triangle(n):
    result = []
    
    for i in range(1, n + 1):
        # Last row → all stars
        if i == n:
            result.append("*" * n)
        else:
            if i == 1:
                result.append("*")
            else:
                # 1 star + spaces + 1 star
                row = "*" + " " * (i - 2) + "*"
                result.append(row)
    
    return result
print(generate_hollow_right_angled_triangle(10))