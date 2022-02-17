from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoForm


def todo_list(request):
    # object is type of django ORM that is used by python packages to access database
    todos = ToDo.objects.all()
    context = {
        'todo_list': todos,
    }
    print(todos)
    return render(request, 'ToDo_list.html', context=context)


# actions that can be preformed on a model database is CRUD [Create, Read, Update, Delete, LIST]

def todo_read(request, id):
    # get the todo object from the database which has an id of id
    todo = ToDo.objects.get(id=id)
    # create a dict to pass the todo object to the template as context
    context = {
        'todo': todo,
    }
    return render(request, 'ToDo_read.html', context=context)


def todo_create(request):
    # create a form object which get data only if post request is made
    form = ToDoForm(request.POST or None)
    # check if posted data is valid like date is in correct format
    if form.is_valid():
        print(form.cleaned_data)
        # save the form data to the database
        name = form.cleaned_data['name']
        duedate = form.cleaned_data['duedate']

        # create new entry to the database
        todo = ToDo.objects.create(name=name, duedate=duedate)

        # redirect to the todo_list page
        return redirect('/')

        # or we can use
        ## form.save(
    context = {
        "form": form,
    }
    return render(request, 'ToDo_create.html', context=context)


def todo_update(request, id):
    # get the todo object with id
    todo_entry = ToDo.objects.get(id=id)

    # get the form
    form = ToDoForm(request.POST or None, instance=todo_entry)

    if form.is_valid():
        form.save()
        return redirect('/')

    context = {
        "form": form,
    }

    return render(request, 'ToDo_update.html', context=context)

def todo_delete(request, id):
    todo_entry = ToDo.objects.get(id=id)
    todo_entry.delete()
    return redirect('/')
