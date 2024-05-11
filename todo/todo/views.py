from django.shortcuts import HttpResponse, render
from django.http import JsonResponse
from .models import Todo

def hello_views(request):
	return HttpResponse(f" <marquee> <h1>Hello world</h1></marquee>")

def list_todo(request):
	db_todos= Todo.objects.all()
	response_todo=[]
	for i in db_todos:
		response_todo.append(
        {"title": i.title, "completed": i.completed,"created_at": i.created_at})
	return JsonResponse(response_todo , safe=False)


def retrive_todo(request, todoId):
	todo= Todo.objects.get(id=todoId)
	return JsonResponse({
		"title": todo.title,
		"completed":todo.completed,
		"created_at" : todo.created_at
},
					 safe=False,)


def update_todo(request, todoId):
	todo= Todo.objects.get(id=todoId)
	todo.completed=True
	todo.save()
	return JsonResponse({
		"title": todo.title,
		"completed":todo.completed,
		"created_at" : todo.created_at
},
					 safe=False,)




def delete_todo(request, todoId):
	todo= Todo.objects.get(id=todoId)

	todo.delete()

	return JsonResponse({"message": "Todo deleted sucessfully"}, safe=False)





def hello_views(request):
	return render(request,  "index.html")


def home_views(request):
	return render(request,  "Home.html")


def index_views(request):
    return render(request, "index.html")


def about(request):
	return HttpResponse("rrrkcckc")
