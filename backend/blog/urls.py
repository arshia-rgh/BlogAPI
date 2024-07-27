from django.urls import path
from .views.crud_views.v1_views import CrudPostView
urlpatterns = [
    path('posts/', CrudPostView.as_view(), name="posts"),
    path('posts/<int:pk>/', CrudPostView.as_view(), name='post'),
]
