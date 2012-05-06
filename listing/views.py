from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SubmitRequest
from .models import ProblemForm
from .models import Problem
from django.contrib.auth.models import User
from accounts.models import UserProfile

@login_required
def submit_request(request): #we dont use this view anywhere, if you wrote it, please delete or comment where we use it
    form = SubmitRequest(request.POST or None)
    if form.is_valid():
        print form
        print dir(form)
        return HttpResponseRedirect('/thanks/')  # Redirect after POST
    return render(request, 'contact.html', {
        'form': form,
    })


def listings(request):
    problems = Problem.objects.all()
    problems_count = Problem.objects.count()
    persons_count = UserProfile.objects.count()

    return render(request, 'listing_problems.html', {
        'problems': problems,
        'persons_count':persons_count,
        'problems_count': problems_count,
        })


def listings_persons(request):
    persons = UserProfile.objects.all()
    persons_count = UserProfile.objects.count()
    problems_count = Problem.objects.count()
    return render(request, 'listing_persons.html', {
        'persons': persons,
        'persons_count':persons_count,
        'problems_count': problems_count,
        })

@login_required
def submit_problem(request):
    form = ProblemForm(request.POST or None)
    form.instance.user = request.user
    if form.is_valid():
        form.save()
        return redirect(listings_persons)
    return render(request, 'forms/submit_problem.html', {
        'form': form,
    })
