"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Book
from django.http import HttpResponse


def book(request,book_detail):
    try:
        findBook = Book.objects.get(pk=book_detail)
    except:
        raise Http404("This book does not exist")
    return HttpResponse("This book name is :  %s" % findBook.title) 

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
