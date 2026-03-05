import re
s = input()
numbers = re.findall(r"\d+", s)
for i in range(len(numbers)):
    if(numbers[i][0] == '8' and numbers[i][1] == '4'):
        numbers[0] = '+' + numbers[0]
    s = s.replace(numbers[i], "{REDACTED}")
print(s)