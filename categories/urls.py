from django.urls import path
from .views import list_category, detail_category

urlpatterns = [
    path('category/', list_category, name='list_category'),
    path('category/<int:pk>', detail_category, name='detail_category')
]