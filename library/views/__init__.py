from .author import AuthorListView
from .author import AuthorDetailView
from .author import AuthorCreateView
from .author import AuthorUpdateView
from .author import AuthorDeleteView

from .books import BooksListView
from .books import BooksDetailView
from .books import BooksCreateView
from .books import BooksUpdateView
from .books import BooksDeleteView

from .reader import ReaderListView
from .reader import ReaderDetailView
from .reader import ReaderCreateView
from .reader import ReaderUpdateView
from .reader import ReaderDeleteView

__all__ = [
    "AuthorListView",
    "AuthorDetailView",
    "AuthorCreateView",
    "AuthorUpdateView",
    "AuthorDeleteView",

    "BooksListView",
    "BooksDetailView",
    "BooksCreateView",
    "BooksUpdateView",
    "BooksDeleteView",

    "ReaderListView",
    "ReaderDetailView",
    "ReaderCreateView",
    "ReaderUpdateView",
    "ReaderDeleteView",
]
