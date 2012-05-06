from django.shortcuts import render
from .forms import SubmitRequest
from .models import ProblemForm
from .models import Problem
from django.contrib.auth.models import User
from accounts.models import UserProfile

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
    
def submit_problem(request):
    form = ProblemForm(request.POST or None)
    if form.is_valid():
        new_problem = form.save()
        new_problem.user = request.user.get_profile()
        new_problem.save()
        return HttpResponseRedirect('listing/people')
    return render(request, 'forms/submit_problem.html', {
        'form': form,
    })
