from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def homepage(request):
    template = loader.get_template('dashboard/homepage.html')
    context = {}
    return HttpResponse(template.render(context, request))