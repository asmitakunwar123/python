
from django.db import models
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
  	path('todos/', include("todo.urls")),
    path('authors/',  include("author.urls")),
 	path('book/',  include("book.urls")),


]


