"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    #Get().route('/', 'WelcomeController@show').name('welcome'),
    Get().route('/', 'BookController@show').name('welcome'),
    
    Post().route('/book/create','BookController@create').name('create'),

    Get('/book/@id/delete','BookController@delete').name('delete'),

    Get('/book/@id/update','BookController@update').name('update'),
    Post('/book/@id/edit','BookController@edit').name('edit')
]
