# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.http import HttpRequest,HttpResponse,JsonResponse,Http404,HttpResponseRedirect
from .models import Question,Choice
from django.db.models import QuerySet
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse

def index(request):
    latest_question_list:QuerySet[Question] = Question.objects.order_by("pub_date")[:5]
    # output = ", ".join([q.question_text for q in latest_question_list])
    template=loader.get_template("polls/index.html")
    context={
        'latest_question_list':latest_question_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id:int):
   question=get_object_or_404(Question,id=question_id)
   return render(request, "polls/detail.html", {"question": question})


def results(request, question_id:int):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response )


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    

