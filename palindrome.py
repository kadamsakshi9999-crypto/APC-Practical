
import string

def is_palindrome(text):
    normalized = ''.join(
        ch.lower() for ch in text
        if ch.isalnum()
    )

    return normalized == normalized[::-1]


text = input("Enter a word or phrase: ")

if is_palindrome(text):
    print("True - It is a palindrome.")
else:
    print("False - It is not a palindrome.")


