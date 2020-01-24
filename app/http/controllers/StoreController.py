"""A StoreController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Book import Book

class StoreController(Controller):
    """StoreController Controller Class."""

    def __init__(self, request: Request):
        """StoreController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        books = Book.all()
        return view.render('store',{'books':books})

    def add(self, request:Request):
        """Add a book and its description"""
        if not request.input('title') and not request.input('description'):
            request.session.flash('warning', 'Empty Title/Description are not accepted!')
        else:
            Book.create(
            title=request.input('title'),
            description=request.input('description')
            )
            request.session.flash('success', 'Book Added!')


        return request.redirect('/')
    
    def delete(self, request:Request):
        book = Book.find(request.param('id'))
        book.delete()
        request.session.flash('danger', 'Book Deleted!')

        return request.redirect('/')

    def update(self, view: View, request: Request):
        book = Book.find(request.param('id'))

        return view.render('update', {'book': book})

    def store(self, request:Request):
        book = Book.find(request.param('id'))

        book.title = request.input('title')
        book.description = request.input('description')

        book.save()
        request.session.flash('sucess', 'Book Updated!')

        return request.redirect('/')