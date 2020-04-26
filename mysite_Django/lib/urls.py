from django.urls import path
from . import views

app_name = 'lib'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('addBook/', views.addBook, name='addBook'),
    path('delBook/<int:book_id>', views.deleteBook, name='delBook')
]
