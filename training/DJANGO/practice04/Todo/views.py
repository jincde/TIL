from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
  todos = Todo.objects.all()

  context = {
    'todos' : todos
  }

  return render(request, 'Todo/index.html', context)

def create(request):
  content = request.GET
  
  if content['priority'] == 'Unrank':
    Todo.object.create(content = content['content'], deadline = content['deadline'])
  else:
    Todo.objects.create(content = content['content'], priority = content['priority'], deadline = content['deadline'])

  return redirect('Todo:index')

def change(request, Todo_pk):
  todo = Todo.objects.get(pk = Todo_pk)

  if todo.completed == True:
    todo.completed = False
  else:
    todo.completed = True

  todo.save()

  return redirect('Todo:index')

def delete(request, Todo_pk):
  todo = Todo.objects.get(pk = Todo_pk)
  todo.delete()

  return redirect('Todo:index')

def update(request, Todo_pk):
  post = Todo.objects.get(pk = Todo_pk)

  content_ = request.GET.get('content')
  priority_ = request.GET.get('priority')
  deadline_ = request.GET.get('deadline')

  post.content = content_
  post.priority = priority_
  post.deadline = deadline_

  post.save()

  return redirect('Todo:index')

# def modify(request, Todo_pk):
#   post = Todo.objects.get(pk = Todo_pk)

#   context = {
#     'post' : post,
#   }
  
#   return render(request, 'Todo/detail.html', context )