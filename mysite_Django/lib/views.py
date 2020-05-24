from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Book
# Create your views here.

def index(request):
    return HttpResponse('Hello Django')

def detail(request):
	book_list = Book.objects.order_by('-pub_date')[:5]
	context = {'book_list': book_list}
	return render(request, 'detail.html', context)

def addBook(request):
	if request.method == 'POST':
		temp_name = request.POST['name']
		temp_author = request.POST['author']
		temp_pub_house = request.POST['pub_house']

	from django.utils import timezone
	temp_book = Book(name=temp_name, author=temp_author, pub_house=temp_pub_house, pub_date=timezone.now())
	temp_book.save()

	return HttpResponseRedirect(reverse('lib:detail'))

def deleteBook(request, book_id):
	bookID = book_id
	Book.objects.filter(id=bookID).delete()
	return HttpResponseRedirect(reverse('lib:detail'))