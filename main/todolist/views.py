from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponse
from .models import task
from datetime import datetime, timedelta

def list(request):
    tasks = task.objects.raw('''
    select task.id, task.title, task.description, task,days ,cast(task.startdate as varchar) as "date", priority.title as "title1"
    from task, priority
     where task.priority =priority.id
     order by priority.title DESC''')
    for t in tasks:
        t.days = (datetime.today() + timedelta(days=t.days)).strftime("%b %d %Y")
    return render(request,'todolist/index.html',{'tasks':tasks})