from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader, RequestContext

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('basicapp/index.html')
    context = {
        'latest_questions': latest_questions
     }
    return render(request, 'basicapp/index.html', context)

def detail(request, question_id):
    return HttpResponse("tHIS IS THE DETAIL VIEW OF THE QUESTION: %s" %question_id)

def results(request, question_id):
    return HttpResponse("These are the results of the question: %s" %question_id)

def vote(request, question_id):
    return HttpResponse("VOTE on question: %s" %question_id)