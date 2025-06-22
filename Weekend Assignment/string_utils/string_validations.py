# String Validations Module

def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Optional: ignore spaces and case
    return s == s[::-1]

def is_alpha(s):
    return s.isalpha()
