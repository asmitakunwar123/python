from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import Book


def Book_view(request):
	books = Book.objects.filter(author__First_name__iexact="jhon")
	response_data = []
	for book in books:
		response_data.append({"title":book.title,
            "author": {
			"first_name": book.author.First_name,
			"last_name": book.author.last_name,
			"age": book.author.age,

                    }
		})
	return JsonResponse(response_data, safe=False)

# def Tag_view(request):
# 	books = Tag.objects.filter(author__First_name__iexact="jhon")
# 	response_Tag = []
# 	for book in books:
# 		response_Tag.append({"title":book.title,
#             "Tag": {
# 			"first_name": book.author.First_name,
# 			"last_name": book.author.last_name,
# 			"age": book.author.age,

#                     }
# 		})
# 	return JsonResponse(response_Tag, safe=False)

