def check_zander_size(size:int):

    size_limit = 42
    if size < size_limit:
        print("The zander is too small. Release it back into the lake.")
        print(f"It is {size_limit - size} cm below the size limit.")
    else:
        print("The zander meets the size limit. You may keep it.")


if __name__ == "__main__":
    size = int(input("Enter the length of the zander (cm): "))
    check_zander_size(size)