def middle_character(text):
    length = len(text)
    middle = length // 2

    if length % 2 == 0:
        return text[middle - 1:middle + 1]
    else:
        return text[middle]

s = input("Enter your string: ")
middle_character(s)