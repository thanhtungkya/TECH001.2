def acronym(phrase):
    words = phrase.split()
    result = ""

    for word in words:
        result += word[0].upper()

    return result

s = input("Enter your string: ")
acronym(s)