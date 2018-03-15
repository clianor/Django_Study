from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':latest_question_list[::-1]
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
    except:
        question = "HTTP 404 Error"
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "지금 %s번 질문의 결과 창을 보고 계십니다."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("지금 %s번 질문의 투표 창을 보고 계십니다." % question_id)