from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect
from .models import *


# 首页，展示所有问题
def index(request):
    lastest_question_list = Questions.objects.all()
    return render(request, "index.html", locals())


# 展示单个问题的所有选项
def detail(req, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(req, "detail.html", locals())


# 查看投票结果，
def results(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, "results.html", locals())


# 选择投票，设置cookie验证
def vote(request, question_id):
    p = get_object_or_404(Questions, pk=question_id)
    if request.COOKIES.get("is_vote", None):
        return render(request, "detail.html", {"question": p, "error_message": "你已经投过票了!"})
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choicing.DoesNotExist):
        return render(request, "detail.html", {"question": p, "error_message": "You did't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        rep = redirect(reverse("voting:results", args=(p.id,)))
        rep.set_cookie("is_vote", True)
        return rep


# Create your views here.
