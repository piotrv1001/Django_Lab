from django.urls import path, include
from .views import delete, index, add, get, update

urlpatterns = [
    path('', index, name="view_books"),
    path('add/', add, name="add"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('<int:id>/', get, name='get'),
]
