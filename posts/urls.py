from django.urls import path
from .views import *

app_name = 'static'

urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("<int:pk>", PostDetailView.as_view(), name="detail"),
    path("create", PostCreateView.as_view(), name="create"),
    path("update/<int:pk>", PostUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", PostDeleteView.as_view(), name="delete"),
]
