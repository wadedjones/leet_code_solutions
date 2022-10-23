#A phrase is a palindrome if, after converting all uppercase letters into lowercase 
# letters and removing all non-alphanumeric characters, it reads the same forward 
# and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

def is_palindrome(s: str) -> bool:
    s_list = [x.lower() for x in s if x.isalnum()]
    s_reversed = list(reversed(s_list))
    return s_list == s_reversed
