def name_age():
    name = input("Enter your name: ")
    birth_year = int(input("Enter your birth year: "))
    print(f"Hello {name}, you are {2025 - birth_year} years old.")

def extract_car_names():
    txt = 'LMaasleitbtui'
    print(txt[::2])

def string_operations():
    s = input("Enter a string: ")
    print(f"Length: {len(s)}, Uppercase: {s.upper()}, Lowercase: {s.lower()}")

def is_palindrome():
    s = input("Enter a string: ")
    print("Palindrome" if s == s[::-1] else "Not a palindrome")

def count_vowels_consonants():
    s = input("Enter a string: ").lower()
    vowels = sum(1 for c in s if c in "aeiou")
    consonants = sum(1 for c in s if c.isalpha() and c not in "aeiou")
    print(f"Vowels: {vowels}, Consonants: {consonants}")

def contains_string():
    s1, s2 = input("Enter two strings: ").split()
    print(s2 in s1)

def word_replace():
    sentence = input("Enter a sentence: ")
    old, new = input("Word to replace: "), input("Replace with: ")
    print(sentence.replace(old, new))

def first_last_char():
    s = input("Enter a string: ")
    print(f"First: {s[0]}, Last: {s[-1]}")

def reverse_string():
    s = input("Enter a string: ")
    print(s[::-1])

def count_words():
    print(len(input("Enter a sentence: ").split()))

def contains_digit():
    print(any(c.isdigit() for c in input("Enter a string: ")))

def join_words():
    words = input("Enter words separated by space: ").split()
    print("-".join(words))

def remove_spaces():
    print(input("Enter a string: ").replace(" ", ""))

def check_equal_strings():
    print(input("Enter first string: ") == input("Enter second string: "))

def acronym():
    print("".join(word[0] for word in input("Enter a phrase: ").split()).upper())

def remove_char():
    s, c = input("Enter a string: "), input("Enter character to remove: ")
    print(s.replace(c, ""))

def replace_vowels():
    print("".join('*' if c in "aeiouAEIOU" else c for c in input("Enter a string: ")))

def check_start_end():
    s = input("Enter a sentence: ")
    start, end = input("Starts with: "), input("Ends with: ")
    print(s.startswith(start) and s.endswith(end))

if __name__ == "__main__":
  name_age()
  extract_car_names()
  string_operations()
  is_palindrome()
  count_vowels_consonants()
  contains_string()
  word_replace()
  first_last_char()
  reverse_string()
  count_words()
  contains_digit()
  join_words()
  remove_spaces()
  check_equal_strings()
  acronym()
  remove_char()
  replace_vowels()
  check_start_end()
