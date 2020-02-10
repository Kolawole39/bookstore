"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    #Get().route('/', 'WelcomeController@show').name('welcome'),
    Get().route('/', 'BookController@show').name('welcome'),
    
    Post().route('/book/create','BookController@create'),

    Get('/book/@id/delete','BookController@delete'),

    Get('/book/@id/update','BookController@update'),
    Post('/book/@id/store','BookController@edit')
]
