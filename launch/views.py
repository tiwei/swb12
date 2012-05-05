from django.shortcuts import render_to_response
from django.template import RequestContext

def index_view(request, template_name='launch/index.html'):
    context = {}
    return render_to_response(template_name, context, RequestContext(request))
