def new_list(a:list[int])->list[int]:
    res = list([])
    for x in a:
        if(x % 2 == 0):
            res.append(x)
    return res

if __name__ == "__main__":
    a = list([1, 2, 3, 4, 5, 5, 5, 2, 2, 2])
    print(new_list(a))