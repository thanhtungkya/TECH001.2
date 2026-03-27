f = "/Users/tungthanhdo/Documents/python/assignment9/bai4.txt"

def caesar_file(filename: str, pos: int, direction: str) -> str:
    if direction == "right":
        shift = pos
    elif direction == "left":
        shift = -pos
    else:
        raise ValueError("direction phải là 'left' hoặc 'right'")

    result = ""

    with open(filename) as f:
        content = f.read()

    for c in content:
        # chữ hoa
        if c.isupper():
            new_c = chr((ord(c) - 65 + shift) % 26 + 65)
            result += new_c

        # chữ thường
        elif c.islower():
            new_c = chr((ord(c) - 97 + shift) % 26 + 97)
            result += new_c

        # số (giữ nguyên)
        elif c.isdigit():
            result += c

        # ký tự khác (space, dấu câu...)
        else:
            result += c

    return result

print(caesar_file(f, 3, "right"))