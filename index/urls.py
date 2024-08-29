from django.urls import path
from index.views import home, single, categories

urlpatterns = [
    path('', home, name='home'),
    path('single/<int:pk>/', single, name='single'),
    path('categories/', categories, name='categories'),
]