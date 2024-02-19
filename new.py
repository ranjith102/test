print 
def is_palindrome(s):
    """
    Check if a string is a palindrome.
    
    Parameters:
        s (str): The string to be checked.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the string with its reverse
    return s == s[::-1]

# Test the function
test_string = "A man, a plan, a canal, Panama!"
print(is_palindrome(test_string))  # Output: True
