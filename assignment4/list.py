def sum_list(a:list)->int:
    res = 0
    for x in a:
        res += x
    return res

if __name__ == "__main__":
    a = list([1, 2, 3, 4, 5])
    print(sum_list(a))