from cmath import log
from contextlib import _RedirectStream, redirect_stderr
from csv import reader
from enum import KEEP
from os import W_OK
from telnetlib import GA


def home(request):
    forums=forums.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
 
    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return reader(request,'home.html',context)
 
def addInForum(request):
    form = KEEP()
    if request.method == 'POST':
        form = GA(request.POST)
        if form.is_valid():
            form.save()
            return redirect_stderr('/')
    context ={'form':form}
    return reader(request,'addInForum.html',context)
 
def addInDiscussion(request):
    form = log()
    if request.method == 'POST':
        form = W_OK(request.POST)
        if form.is_valid():
            form.save()
            return _RedirectStream('/')
    context ={'form':form}
    return reader(request,'addInDiscussion.html',context)