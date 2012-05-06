from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
#from core_models.models import Skill
from .forms import ProfileForm
from .models import UserProfile


@login_required
def profile_view(request, template_name='profile.html'):
    profile = request.user.get_profile()
    skill_list = profile.skills_offered.all()
    form = ProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
    context = {
        'skill_list': skill_list,
        'form': form,
        'profile': profile,
    }
    return render_to_response(template_name, context, RequestContext(request))


def profile_show_view(request, profile_id, template_name='profile_show.html'):
    profile = UserProfile.objects.get(id=profile_id)
    context = {
        'profile': profile,
    }
    return render_to_response(template_name, context, RequestContext(request))
