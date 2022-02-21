from django.shortcuts import render, redirect
# from django.contrib import messages
from todo.models import Todo
from todo.forms import TodoForm


# Create your views here.

def index(request):
    todo_list = Todo.objects.order_by("-date")
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)  # all the form date accessed in form object
        if form.is_valid():
            form.save()
        return redirect('todo')
    context = {
            'title': "TODO LIST",
            'list': todo_list,
            'forms': form,
        }
    return render(request, "todo/index.html", context)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    # messages.info(request, "item removed !!!")
    return redirect('todo')
