from django.shortcuts import render
from .forms import SubmitRequest
from .models import ProblemForm
from .models import Problem

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
    return render(request, 'listing_problems.html', {
        'problems': problems,
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
