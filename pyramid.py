def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    # Your code here
    result=[]
    for i  in range(n):
        spaces=' '*(n-i-1)
        stars="*"*(2*i+1)
        result.append(spaces+stars+spaces)
    return result
print(generate_pyramid(5))