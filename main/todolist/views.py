from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponse
from .models import task
from datetime import datetime, timedelta
from django.db import connection

def list(request):
    UrgantlyList = []
    notUrgantlylist = []
    tasks = task.objects.raw('''
    select task.id, task.title, task.description, task.days ,cast(task.startdate as varchar) as "date", priority.title as "title1"
    from task, priority
     where task.priority =priority.id
     order by priority.title DESC''')
    for t in tasks:
        t.days =  str((datetime.today() + timedelta(days=t.days)) - datetime.strptime(t.date,"%Y-%m-%d")).split(' ')[0] #(datetime.today() + timedelta(days=t.days)).strftime("%b %d %Y")
        if t.title1 == 'Urgantly':
            if int(t.days) < 5:
                UrgantlyList.append(t)
            else:
                notUrgantlylist.append(t)
        else:
            if int(t.days) < 15:
                UrgantlyList.append(t)
            else:
                notUrgantlylist.append(t)
    return render(request,'todolist/index.html',{'Urgantly':UrgantlyList,'NotUrgantly':notUrgantlylist})


def apply(request,id):
    with connection.cursor() as cursor:
        cursor.execute(f'''
        insert into applied(title,description,days)
select task.title, task.description, task.startdate-current_date from task where id = {id}''')
        cursor.execute('DELETE FROM task where id ='+str(id))

    return redirect('list')


def new(request):
    if request.method == 'POST':
        title = request.POST.get('title',None)
        description = request.POST.get('description', None)
        description = request.POST.get('description', None)
        days = request.POST.get('days', None)
        priority = request.POST.get('priority', None)
        p = 1
        if priority == 'Not urgantly':
            p = 2
        with connection.cursor() as cursor:
            cursor.execute(f'''
            insert into task(title,description,startdate,priority,days) 
            Values('{title}',
            '{description}',
            to_date('{datetime.today()}','YYYY-MM-DD'),
            {p},
            {days}) 
            ''')
        return redirect('list')
    else:
        return render(request,'todolist/new.html')


def appliedlist(request):
    tasks = task.objects.raw('''
        select * from applied''')
    return render(request,'todolist/applied.html',{'tasks':tasks})


def remove(request,id):
    cursor.execute('DELETE FROM task where id =' + str(id))

    return redirect('list')