s = input()
def sum_number_in_str(s:str)->int:
    sum = 0
    tmp = 0
    for i in range(len(s)):
        if(s[i].isdigit()):
            tmp = tmp * 10 + int(s[i])
        else:
            sum += tmp
            tmp = 0
    return sum

print(sum_number_in_str(s))