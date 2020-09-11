from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from todo_app.models import Tasklist
from todo_app.forms import TaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

#def todo(request):
  #  return HttpResponse("Welcome to My first page.")


@login_required
def todo(request):
    form = None
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
        messages.success(request,'New Task Added!')
        return redirect('todo')
    else:
        allobjects = Tasklist.objects.filter(owner=request.user)
        paginator = Paginator(allobjects,2)
        page = request.GET.get('pg')
        allobjects = paginator.get_page(page)
        return render(request,'todo.html',{'allobjects':allobjects})

@login_required
def delete_task(request,task_id):
    deleteItem = Tasklist.objects.get(pk=task_id)
    if deleteItem.owner == request.user:
        deleteItem.delete()
    else:
        messages.error(request,("This actions is restricted for you!Please login and then try."))    
    return redirect('todo')

@login_required
def complete_task(request,task_id):
    itemStatus= Tasklist.objects.get(pk=task_id)
    if deleteItem.owner == request.user:
        itemStatus.jobStatus = True
        itemStatus.save()
    else:
        messages.error(request,("This actions is restricted for you!Please login and then try."))    
    return redirect('todo')

@login_required
def markPending_task(request,task_id):
    itemStatus= Tasklist.objects.get(pk=task_id)
    itemStatus.jobStatus = False
    itemStatus.save()
    return redirect('todo')

@login_required    
def edit_task(request,task_id):
    obj_task = Tasklist.objects.get(pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST or None,instance=obj_task)
        if form.is_valid():
            form.save()
        messages.success(request,'Task is updated!')
        return redirect('todo')
    else:
        return render(request,'edit.html',{'obj_task':obj_task})

@login_required
def home(request):
    return render(request,'home.html',{'Home_text':'Welcome to Home page.'})        

@login_required  
def index(request):
    return render(request,'index.html',{'index_text':'Welcome to Home page.'})        
    

def contactus(request):
    return render(request,'contactus.html',{'Contact_text':'Welcome to Contact Us page.'})  
