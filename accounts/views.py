from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
#from core_models.models import Skill


@login_required
def profile_view(request, template_name='accounts/profile.html'):
    skill_list = request.user.get_profile().skills_offered.all()
    context = {
        'skill_list': skill_list,
    }
    return render_to_response(template_name, context, RequestContext(request))
