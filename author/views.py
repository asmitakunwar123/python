from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import Author


def author_view(request):
	authors = Author.objects.filter(First_name='Jhon')
	# print("\n")
	# print(authors)
	# print("\n")
	response_author = []
	for i in authors:
		response_author.append({
		"First_name": i.First_name,
		"last_name": i.last_name,
		"age": i.age,
			})
		return JsonResponse(response_author, safe=False)

