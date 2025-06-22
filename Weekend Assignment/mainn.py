# Main program using string_utils package

from string_utils import string_operations as ops
from string_utils import string_validations as val

def main():
    s = input("Enter a string: ")
    print("Reversed String:", ops.reverse_string(s))
    print("Uppercase:", ops.to_uppercase(s))
    print("Length:", ops.string_length(s))

    print("Is Palindrome:", val.is_palindrome(s))
    print("Contains Only Alphabets:", val.is_alpha(s))

if __name__ == "__main__":
    main()
