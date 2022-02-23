from django.urls import include, path
from rest_framework import routers

from backend.todo import views as V
from backend.todo.api.viewsets import TodoViewSet

app_name = 'todo'
router = routers.DefaultRouter()
routers.register(r'todos', TodoViewSet)

urlpatterns = [
    path('', v.TodoListVIew.as_view(), name='todo_list'),
    path('<int:pk>/', v.TodoDetailView.as_view(), name='todo_detail'),
    path('create/', v.TodoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/update/', v.TodoUpdateView.as_view(), name='todo_update'),
    path('<int:pk>/delete/', v.TodoDeleteView.as_view(), name='todo_delete'),
]

urlpatterns=[
    path('todos/', include(todo_urlpatterns)),
    path('api/v1', include(router.urls)),
    ]


