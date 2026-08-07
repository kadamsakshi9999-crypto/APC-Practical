#1.String Length
"""
string = input("Enter a string: ")

count = 0

for ch in string:
    count += 1

print("Length of the string =", count)
"""


#2.Character Count
"""
string = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in string:
    if ch in "AEIOUaeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special Characters =", special)
"""


#3.Reverse a String
"""
string = input("Enter a string: ")

reverse = ""

for i in range(len(string)-1, -1, -1):
    reverse += string[i]

print("Reversed String =", reverse)
"""


#4.Palindrome Check
"""
string = input("Enter a string: ")

reverse = ""

for i in range(len(string)-1, -1, -1):
    reverse += string[i]

if string == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
"""


#5.Uppercase and Lowercase Count
"""
string = input("Enter a string: ")

upper = 0
lower = 0

for ch in string:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase Letters =", upper)
print("Lowercase Letters =", lower)
"""


#6.Replace Characters
"""
string = input("Enter a string: ")

old = input("Enter character to replace: ")
new = input("Enter new character: ")

result = ""

for ch in string:
    if ch == old:
        result += new
    else:
        result += ch

print("New String =", result)
"""


#7.Remove Spaces
"""
string = input("Enter a string: ")

result = ""

for ch in string:
    if ch != " ":
        result += ch

print("String without spaces =", result)
"""


#8.Frequency of a Character
"""
string = input("Enter a string: ")

ch = input("Enter character: ")

count = 0

for i in string:
    if i == ch:
        count += 1

print("Frequency =", count)
"""


#9.First and Last Character
"""
string = input("Enter a string: ")

print("First Character =", string[0])
print("Last Character =", string[-1])
"""


#10.ASCII Values
"""
string = input("Enter a string: ")

for ch in string:
    print(ch, "=", ord(ch))
"""

#11.Word Count
"""
sentence = input("Enter a sentence: ")

words = sentence.split()

count = 0

for word in words:
    count += 1

print("Total Words =", count)
"""


#12.Longest Word
"""
sentence = input("Enter a sentence: ")

words = sentence.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest Word =", longest)
"""


#13.Shortest Word
"""
sentence = input("Enter a sentence: ")

words = sentence.split()

shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest Word =", shortest)
"""


#14.Title Case
"""
sentence = input("Enter a sentence: ")

words = sentence.split()

result = ""

for word in words:
    result += word[0].upper() + word[1:].lower() + " "

print("Title Case =", result)
"""


#15.Duplicate Characters
"""
string = input("Enter a string: ")

printed = ""

for i in range(len(string)):
    count = 0

    for j in range(len(string)):
        if string[i] == string[j]:
            count += 1

    if count > 1 and string[i] not in printed:
        print(string[i])
        printed += string[i]
"""


#16.Character Frequency
"""
string = input("Enter a string: ")

printed = ""

for ch in string:
    if ch not in printed:
        count = 0

        for i in string:
            if ch == i:
                count += 1

        print(ch, "=", count)
        printed += ch
"""


#17.Anagram Check
"""
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if sorted(string1) == sorted(string2):
    print("Anagram")
else:
    print("Not Anagram")
"""


#18.Remove Duplicate Characters
"""
string = input("Enter a string: ")

result = ""

for ch in string:
    if ch not in result:
        result += ch

print("New String =", result)
"""


#19.Substring Search
"""
string = input("Enter main string: ")

sub = input("Enter substring: ")

if sub in string:
    print("Substring Found")
else:
    print("Substring Not Found")
"""


#20.Count Occurrences of a Word
"""
sentence = input("Enter a sentence: ")

word = input("Enter word to search: ")

words = sentence.split()

count = 0

for w in words:
    if w == word:
        count += 1

print("Occurrences =", count)
"""

#21.Password Validator
"""
password = input("Enter Password: ")

upper = 0
lower = 0
digit = 0
special = 0

for ch in password:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1

if len(password) >= 8 and upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
    print("Valid Password")
else:
    print("Invalid Password")
"""


#22.Run-Length Encoding
"""
string = input("Enter a string: ")

result = ""
count = 1

for i in range(len(string)):
    if i < len(string) - 1 and string[i] == string[i + 1]:
        count += 1
    else:
        result += string[i] + str(count)
        count = 1

print("Encoded String =", result)
"""


#23.String Compression
"""
string = input("Enter a string: ")

compressed = ""
count = 1

for i in range(len(string)):
    if i < len(string) - 1 and string[i] == string[i + 1]:
        count += 1
    else:
        compressed += string[i] + str(count)
        count = 1

if len(compressed) < len(string):
    print("Compressed String =", compressed)
else:
    print("Original String =", string)
"""


#24.Most Frequent Character
"""
string = input("Enter a string: ")

max_count = 0
max_char = ""

for ch in string:
    count = 0

    for i in string:
        if ch == i:
            count += 1

    if count > max_count:
        max_count = count
        max_char = ch

print("Most Frequent Character =", max_char)
print("Frequency =", max_count)
"""


#25.Second Most Frequent Character
"""
string = input("Enter a string: ")

freq = {}

for ch in string:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

first = ""
second = ""
first_count = 0
second_count = 0

for ch in freq:
    if freq[ch] > first_count:
        second = first
        second_count = first_count
        first = ch
        first_count = freq[ch]
    elif freq[ch] > second_count:
        second = ch
        second_count = freq[ch]

print("Second Most Frequent Character =", second)
print("Frequency =", second_count)
"""


#26.Caesar Cipher
"""
text = input("Enter Message: ")
shift = int(input("Enter Shift Value: "))

encrypted = ""

for ch in text:
    if ch.isalpha():
        if ch.isupper():
            encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            encrypted += chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        encrypted += ch

print("Encrypted Message =", encrypted)

decrypted = ""

for ch in encrypted:
    if ch.isalpha():
        if ch.isupper():
            decrypted += chr((ord(ch) - 65 - shift) % 26 + 65)
        else:
            decrypted += chr((ord(ch) - 97 - shift) % 26 + 97)
    else:
        decrypted += ch

print("Decrypted Message =", decrypted)
"""


#27.Email Validator
"""
email = input("Enter Email: ")

if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Valid Email")
else:
    print("Invalid Email")
"""


#28.Word Frequency Dictionary
"""
paragraph = input("Enter Paragraph: ")

words = paragraph.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

for word in freq:
    print(word, "=", freq[word])
"""


#29.Sentence Reversal
"""
sentence = input("Enter a sentence: ")

words = sentence.split()

for i in range(len(words)-1, -1, -1):
    print(words[i], end=" ")
"""


#30.String Rotation
"""
string1 = input("Enter First String: ")
string2 = input("Enter Second String: ")

if len(string1) == len(string2) and string2 in (string1 + string1):
    print("Yes, It is a Rotation")
else:
    print("No, It is Not a Rotation")
"""
