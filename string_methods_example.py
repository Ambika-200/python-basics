# String Examples in Python

name = "  Ambika M  "


# 1️ Types
print("Type of name:", type(name))   # type()
print("Convert number to string:", str(123))  # str()


# 2️ Math
print("Length of name:", len(name))  # len()
print("Count of 'a':", name.count('a'))  # count()


# 3️ Transformations
print("Replace M with K:", name.replace("M", "K"))  # replace()
print("Join 'H' + 'i':", 'H' + 'i')  # Concatenation
age = 19
print(f"My name is {name.strip()} and I'm {age} years old")  # f{}
print("Split by space:", name.split())  # split()
print("'ha' * 2:", 'ha' * 2)  # repetition

# 4 Extraction
word = "cat"
print("word[0]:", word[0])     # 'c'
print("word[1:3]:", word[1:3]) # 'at'


# 5 Cleaning - Whitespaces
print("Left Strip:", name.lstrip())   # lstrip()
print("Right Strip:", name.rstrip())  # rstrip()
print("Both Strip:", name.strip())    # strip()


#  Cleaning - Case
print("Lowercase:", name.lower())  # lower()
print("Uppercase:", name.upper())  # upper()




