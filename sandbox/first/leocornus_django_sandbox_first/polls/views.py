from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.template import loader

from .models import Question

# Create your views here.

def index(request):

    # get the lastest five questions.
    questions = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'latest_question_list' : questions,
    })
    return HttpResponse(template.render(context))

