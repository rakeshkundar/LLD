from library_aggregator import Library


if __name__ == '__main__':
    books = ['A', 'B', 'C', 'D', 'E']
    lib = Library(books)
    iterator = lib.createIterator()

    while(iterator.has_next()):
        print(f"Element : {iterator.next()}")
        
