def read_bible_lines(num=10):
    text = ""
    with open("book_part1.txt", "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i > num:
                return text
            text += line
    return text