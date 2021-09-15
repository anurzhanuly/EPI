def author_h_index(book_titles: list, book_citations: list)-> int:
    counter: int = 1

    for _ in book_citations:
        tmp: int = 0

        for number in book_citations:
            if counter <= number:
                tmp += 1
        
        if tmp < counter:
            break

        counter += 1

    return counter-1

print(author_h_index([], [1, 2, 3, 4, 5]))
print(author_h_index([], [4, 4, 4, 4, 5]))
print(author_h_index([], [1, 2, 2, 1, 0]))