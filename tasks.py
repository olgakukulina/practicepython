# 1
base_string = str(input())
base_string_1 = base_string.replace(" ", "_")
print(base_string_1)

# 2
text = input()
word_count = 0
in_word = False
for char in text:
    if char == ' ':
        if in_word:
            in_word = False
    else:
        if not in_word:
            word_count += 1
            in_word = True
print(f"Количество слов в строке: {word_count}")

#  3
base_string = input()
words = []
current_word = ""
for char in base_string:
    if char != " ":
        current_word += char
    else:
        if current_word:
            words.append(current_word)
            current_word = ""
if current_word:
    words.append(current_word)
reversed_words = []
for word in words:
    reversed_words.append(word[::-1])
print(*reversed_words, sep=" ")

#  4
str1 = input()
str2 = input()
if abs(len(str1) - len(str2)) == 2:
    print(False)
else:
    found = False
    for i in range(len(str1)):
        new_str = str1[:i] + str1[i + 1:]
        if new_str == str2:
            found = True
            break
    print(found)

# 5
base_string_5_1 = input()
base_string_5_2 = input()
max_common_string = ""
max_common_string_length = 0
for i in range(len(base_string_5_1)):
    for j in range(i + 1, len(base_string_5_1) + 1):
        current_substring = base_string_5_1[i:j]
        if current_substring in base_string_5_2:
            if len(current_substring) > max_common_string_length:
                max_common_string_length = len(current_substring)
                max_common_string = current_substring
print(max_common_string)
