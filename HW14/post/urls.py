from django.urls import path
from .views import HomeView, DetailView, DeleteView, CreateView, UpdateView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<str:post_title>', DetailView.as_view(), name='details'),
    path('delete/<str:post_title>', DeleteView.as_view(), name='delete'),
    path('update/<str:post_title>', UpdateView.as_view(), name='update'),
    path('create/', CreateView.as_view(), name='create'),
]
