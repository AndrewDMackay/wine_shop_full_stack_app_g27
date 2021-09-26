import pdb

from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("J.R.R. Tolkein")
author_repository.save(author1)

author2 = Author("Christopher, and J.R.R. Tolkein")
author_repository.save(author2)

author_repository.select_all()

book1 = Book("The Lord Of The Rings", author1)
book_repository.save(book1)

book2 = Book("The Hobbit", author1)
book_repository.save(book2)

book3 = Book("The Silmarillion", author2)
book_repository.save(book3)


pdb.set_trace()