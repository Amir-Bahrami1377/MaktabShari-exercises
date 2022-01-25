from django.urls import path
from .views import home, detail, delete, create, update


urlpatterns = [
    path('', home, name='home'),
    path('detail/<str:post_title>', detail, name='details'),
    path('delete/<str:post_title>', delete, name='delete'),
    path('update/<str:post_title>', update, name='update'),
    path('create/', create, name='create'),
]
