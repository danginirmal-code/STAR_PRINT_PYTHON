def generate_inverted_pyramid(n):
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the inverted pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.
    """
    result=[]
    for i in range(n):
        spaces=' '*i
        stars="*"*(2*(n-i)-1)
        result.append(spaces+stars+spaces)
    return result
print(generate_inverted_pyramid(5))

