from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Skill

def profile_view(request, template_name='accounts/profile.html'):
    context = {}
    return render_to_response(template_name, context, RequestContext(request))
