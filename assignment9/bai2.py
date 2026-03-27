def find_keyword_lines(file_path, keyword):
    """Return a list of 1-based line numbers where `keyword` appears in the file."""
    line_numbers = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f, 1):
            if keyword in line:
                line_numbers.append(idx)
    return line_numbers


if __name__ == '__main__':
    path = '/Users/tungthanhdo/Documents/python/assignment9/bai2.txt'
    word = 'Tung'
    print(find_keyword_lines(path, word))
