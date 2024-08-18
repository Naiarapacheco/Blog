from django.urls import path

from .views import detail, delete_comment

urlpatterns = [
    path('<slug:slug>/', detail, name='details'),
    path('comment/<int:id>/', delete_comment, name="delete_comment")
]