from django.urls import path, include
from basiccrud.views import TaskList, TodoListCreateView

urlpatterns = [
    path('get-tasks/', TodoListCreateView.as_view(), name='get-tasks'),
    path('delete-task/<str:id>', TaskList.as_view(), name='delete-task'),
    path('put-task/<str:id>', TaskList.as_view(), name='put-tasks'),
]
