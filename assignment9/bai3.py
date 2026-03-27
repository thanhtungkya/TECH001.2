def average_score(file_path):
    total = 0
    count = 0

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) != 2:
                raise ValueError(f"Invalid line format: {line}")
            name, score_str = parts
            try:
                score = float(score_str)
            except ValueError:
                raise ValueError(f"Invalid score value for {name.strip()}: {score_str}")
            total += score
            count += 1

    if count == 0:
        return 0.0
    return total / count


if __name__ == '__main__':
    path = "/Users/tungthanhdo/Documents/python/assignment9/bai3.txt"
    avg = average_score(path)
    print(f"Average score: {avg:.2f}")
