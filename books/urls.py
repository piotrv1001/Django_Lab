from django.urls import path, include
from .views import index, add, get, update

urlpatterns = [
    path('', index, name="view_books"),
    path('add/', add, name="add"),
    path('update/', update, name="update"),
    path('<int:id>/', get, name='get'),
]
