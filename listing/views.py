from django.shortcuts import render
from core_models.models import Problem
from .forms import SubmitRequest


def submit_request(request):
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
    return render(request, 'listing.html', {
        'problems': problems,
        })
    
def submit_problem(request):
    form = ProblemForm(request.POST or None)
    if form.is_valid():
        new_problem = form.save()
    return render(request, 'submit_problem.html', {
        'form': form,
    })
