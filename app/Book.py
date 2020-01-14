"""Book Model."""

from config.database import Model


class Book(Model):
    """Book Model."""
    __table__ = 'books'
    __fillable__=['title','description']