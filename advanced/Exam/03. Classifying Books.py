def classify_books(*args, **kwargs):
    id_books = {title: num for num, title in kwargs.items()}
    fiction_books = {}
    nonfiction_books = {}
    for genre, title in args:
        if genre == "fiction":
            fiction_books[title] = id_books[title]
        else:
            nonfiction_books[title] = id_books[title]

    sorted_fiction_books = dict(sorted(fiction_books.items(), key=lambda x: x[1]))
    sorted_nonfiction_books = dict(sorted(nonfiction_books.items(), key=lambda x: x[1], reverse=True))

    result = []
    if sorted_fiction_books:
        result.append("Fiction Books:")
        for title, num in sorted_fiction_books.items():
            result.append(f"~~~{num}#{title}")
    if sorted_nonfiction_books:
        result.append('Non-Fiction Books:')
        for title, num in sorted_nonfiction_books.items():
            result.append(f"***{num}#{title}")

    return "\n".join(result)
