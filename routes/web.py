"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    #Get().route('/', 'WelcomeController@show').name('welcome'),
    Get().route('/', 'StoreController@show').name('welcome'),
    
    Post().route('/add','StoreController@add'),

    Get('/@id/delete','StoreController@delete'),

    Get('/@id/update','StoreController@update'),
    Post('/@id/store','StoreController@store')
]
