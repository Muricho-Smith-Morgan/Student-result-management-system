from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from .models import Mark
from django.contrib import messages
from django.template import loader
from .forms import EditForm, EditStudentInfoForm, EditCaseInfoForm

# Create your views here.
def admin(request):
    return render(request, 'myapp/admin.html',)

def admin_panel(request):
    return render(request, 'myapp/admin_panel.html',)

def add_student(request):
    form = EditCaseInfoForm()
    if request.method == 'POST':
        form = EditCaseInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, ' details updated successfully.')
            return redirect('declare')

    context = {'form': form}
    return render(request, 'myapp/add_student.html', context)


def result(request):
    mydata = Mark.objects.all()
    context = {'mymembers': mydata}
    return render(request, 'myapp/result.html', context)

def declare(request):
    mydata = Mark.objects.all()
    context = {'mymembers': mydata}
    return render(request, 'myapp/declare.html', context)

def index(request):
    return render(request, 'myapp/index.html',)

def edit(request, pk):
    student = Mark.objects.get(id=pk)
    form = EditForm(instance=student)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('declare')
        

    context = {'edit_form': form}
    return render(request, 'myapp/edit.html', context)

def print(request, pk):
    obj = Mark.objects.get(id=pk)
    form = EditCaseInfoForm()
    if request.method == 'POST':
        form = EditCaseInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, ' details updated successfully.')
            return redirect('response')

    context = {'form': form}
    return render(request, 'myapp/print.html', context)




def delete(request, pk):
    obj = Mark.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        messages.error(request, 'Mark details deleted successfully.')
        return redirect('declare')

    context = {'obj': obj}
    return render(request, 'myapp/delete.html', context)


def professor(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Password = request.POST['password']
        user = auth.authenticate(username = Username, password = Password)

        if user is not None:
            auth.login(request, user)
            return redirect('admin_panel')
        else:
            messages.error(request, 'Invalid details')
            return redirect('professor')

    return render(request, 'myapp/professor.html',)

def student(request):

    if request.method == 'POST':
        Username = request.POST['username']
        Password = request.POST['password']
        user = auth.authenticate(username = Username, password = Password)

        if user is not None:
            auth.login(request, user)
            return redirect('result')
        else:
            messages.error(request, 'Invalid details')
            return redirect('student')
    return render(request, 'myapp/student.html',)