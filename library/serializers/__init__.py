from .reader import ReaderListSerializer
from .reader import ReaderDetailSerializer
from .reader import ReaderCreateSerializer
from .reader import ReaderUpdateSerializer
from .reader import ReaderDeleteSerializer

from .author import AuthorListSerializer
from .author import AuthorDetailSerializer
from .author import AuthorCreateSerializer
from .author import AuthorUpdateSerializer
from .author import AuthorDeleteSerializer

from .books import BooksListSerializer
from .books import BooksDetailSerializer
from .books import BooksCreateSerializer
from .books import BooksUpdateSerializer
from .books import BooksDeleteSerializer


__all__ = [
    "ReaderListSerializer",
    "ReaderDetailSerializer",
    "ReaderCreateSerializer",
    "ReaderUpdateSerializer",
    "ReaderDeleteSerializer",

    "AuthorListSerializer",
    "AuthorDetailSerializer",
    "AuthorCreateSerializer",
    "AuthorUpdateSerializer",
    "AuthorDeleteSerializer",

    "BooksListSerializer",
    "BooksDetailSerializer",
    "BooksCreateSerializer",
    "BooksUpdateSerializer",
    "BooksDeleteSerializer",
]
