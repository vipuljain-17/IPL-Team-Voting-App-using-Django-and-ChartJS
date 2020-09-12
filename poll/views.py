from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import PollForm, QuestionForm
from .models import Question

from django.db.models import Count


def give():
    total = Question.objects.count()
    a = Question.objects.values('team').order_by('team').annotate(count = Count('team'))
    #print(list(a))
    return total,a


# Create your views here.
def home_view(request, *args, **kwargs):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(result_view)
    
    form = QuestionForm()
    context = {"form":form}
    return render(request,"home.html",context)

def result_view(request, *args, **kwargs):
    total, a = give()
    context = {
        "total":total,
        "a": a}
    return render(request, "result.html",context)

def about_view(request, *args, **kwargs):
    return render(request, "about.html",context={})