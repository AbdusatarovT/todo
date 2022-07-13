from django.shortcuts import render
from rest_framework.generics import *
from todo.models import Task
from todo.serializers import TaskSerializer


# class TaskListView(ListAPIView): #получает все из queryset
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#
# class TaskCreateView(CreateAPIView):# для создания
#     serializer_class = TaskSerializer
#
#
# class TaskDetailView(RetrieveAPIView): # для вывода информации
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     lookup_field = 'id' # если хотим работать именно с id а так можно pk
#
#
# class TaskUpdateView(UpdateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#
# class TaskDeleteView(DestroyAPIView): # для удоления
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer



class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
