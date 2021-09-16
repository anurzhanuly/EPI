def author_h_index(book_titles: list, book_citations: list)-> int:
    book_citations = sorted(book_citations)
    books_count: int = len(book_citations)
    result: int

    for i, value in enumerate(book_citations):
        if value <= books_count - i:
            result = value

    return result


print(author_h_index([], [1, 2, 3, 4, 5]))
print(author_h_index([], [1, 1, 1, 3, 4, 6, 2, 3, 4, 5]))
print(author_h_index([], [4, 4, 4, 4, 5]))
print(author_h_index([], [1, 2, 2, 1, 0]))