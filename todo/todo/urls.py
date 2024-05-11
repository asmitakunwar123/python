
from django.urls import path
from .views import hello_views, home_views, index_views, retrive_todo, list_todo, update_todo, delete_todo
# from .views import list_users, update_users

urlpatterns = [

  	 path('', home_views),
    path('hello/', hello_views),
    path('index/', index_views),
   	path('todo/<int:todoId>/', retrive_todo),
   	path('todo/<int:todoId>/update/', update_todo),
   	path('todo/<int:todoId>/delete/', delete_todo),
    path('todos/', list_todo),
    # path('users/', list_users),
   	# # path('user/<int:userId>/update/', update_users),

]
