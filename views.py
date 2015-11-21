from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from .models import *

def forum(request):
    post = Post.objects.all()
    template = loader.get_template("forum.html")
    context = RequestContext(request, {
        'post': post
    })

    return HttpResponse(template.render(context))
