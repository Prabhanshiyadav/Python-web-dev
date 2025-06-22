def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():  # Check if it's a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count
user_input = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(user_input)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
