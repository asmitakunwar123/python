
from django. urls import path
from .views import Book_view
urlpatterns = [
    path("", Book_view)
]
