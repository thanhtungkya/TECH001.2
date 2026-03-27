def count_non_empty_lines(filename: str) -> int:
    count = 0

    with open(filename, "r") as f:
        for line in f:
            if line.strip() != "":   # bỏ qua dòng trống
                count += 1

    return count

print(count_non_empty_lines("/Users/tungthanhdo/Documents/python/assignment9/bai1.txt"))  # 3