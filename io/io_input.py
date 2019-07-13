import re


def reverse(text):
    return text[::-1]

def is_palindrome(text):
    #Remove all punctuation and spaces
    no_forbidden_text = re.sub(r'[\.\?!:;\-_\(\)\[\]\'\"/,\s]','', text )
    return no_forbidden_text.lower() == reverse(no_forbidden_text.lower())

something = input("Enter text: ")

if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")