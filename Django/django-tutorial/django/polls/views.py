from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, Http404 
from django.urls import reverse

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('poll:results', args=(question_id,)))

def add_choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        add_choice=request.POST['add']
        if add_choice =="":
            raise KeyError
    except (KeyError):
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't input string."
            })
    question.choice_set.create(choice_text=add_choice,votes=0)
    return HttpResponseRedirect(revers('poll:detail', args=(question_id,)))
