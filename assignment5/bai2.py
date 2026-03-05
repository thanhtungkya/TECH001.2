s = input()
def check_color_code(s:str)->bool:
    if(s[0] != '#'):
        return False
    for i in range(1, len(s)):
        check = s[i].isdigit() or ('a' <= s[i] <= 'f')
        if(not check):
            return False
    return True

if(check_color_code(s)):
    print("True")
else:
    print("No")