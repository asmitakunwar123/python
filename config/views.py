# from django.shortcuts import HttpResponse, render
# from django.http import JsonResponse
# def hello_views(request):
# 	return HttpResponse(f" <marquee> <h1>Hello world</h1></marquee>")

# todos =[{
#  "userId": 1, "id": 1, "title": "Buy milks", "completed":False},
# {
#     "userId": 1, "id": 2, "title": "Buy coffee ", "completed": False},
# {
#     "userId": 1, "id": 3, "title": "Buy pen ", "completed": False}]

# def list_todo(request):

# 	return JsonResponse(todos, safe=False)
# def retrive_todo(request,todoId):
# 	print(f"todoId:{todoId}")

# 	todo=None

# 	for i in todos:
# 		if i['id']==todoId:
# 			todo=i
# 			break
# 		print(todo)


# 	return JsonResponse(todo, safe=False)
# def update_todo(request,todoId):


# 	todo = None

# 	for i in todos:
# 		if i['id'] == todoId:
# 			todo = i
# 			todos.remove(todo)
# 			break
# 	if todo is not None:
# 		todo["completed"]== True
# 		todos.append(todo)
# 		return JsonResponse(todo,{"message":"updated  sucessful"}  ,safe=False)

# 	else:
# 		return JsonResponse({"message":"Not Found"} ,safe=False)

# def delete_todo(request,todoId):
# 	todo = None

# 	for i in todos:
# 		if i['id'] == todoId:
# 			todo = i
# 			todos.remove(todo)
# 			break
# 	if todo is not None:
# 		return JsonResponse({"message":f"Todo with id {todoId} delete"},safe=False)
# 	else:
# 		return JsonResponse({"message":"Not found" } ,safe=False)


# users = [{
#     "userId": 1, "id": 1, "fristname": "Asmita", "lastname": "kunwar", "completed": False},
#     {
#     "userId": 1, "id": 2, "fristname": "Durga", "lastname": "kunwar", "completed": False},
#     {
#     "userId": 1, "id": 3, "fristname": "Devi", "lastname": "kunwar", "completed": False},]


# def list_users(request):

# 	return JsonResponse(users, safe=False)


# def update_users(request, userId):

# 	user = None

# 	for i in users:
# 		if i['id'] == userId:
# 			user = i
# 			users.remove(user)
# 			break
# 	if user is not None:
# 		user["completed"] == True
# 		users.append(user)
# 		return JsonResponse(user, safe=False)
# 	else:
# 		return JsonResponse({"message": "Not Found"}, safe=False)





# def hello_views(request):
# 	return render(request,  "index.html")
# def home_views(request):
# 	return render(request,  "Home.html")


# def index_views(request):
#     return render(request, "index.html")
# def about(request):
# 	return HttpResponse("rrrkcckc")


# def contact_views(request):
# 	return render( request ,"contact.html")


