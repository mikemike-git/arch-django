from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Question, Choice


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "uploader/index.html", context)

def detail(request, question_id):    
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "uploader/detail.html", {"question":question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    try: selected_choice = Question.choice_set.get(pk=request.POST["choice"])
        except (KeyError, Choice.DoesNotExist):
            raise Http404("Sorry!")
            #redisplay the question voting form.
            return render(
                    request,
                    "uploader/detail.html",
                    {
                        "question": question,
                        "error_message": "You didn't select a choice.",
                        },
                    )
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return
        HttpResponseRedirect(reverse("uploader:results", args=(question.id,)))


