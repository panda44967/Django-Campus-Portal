from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice


# ──────────────────────────────────────────────
# / ── ListView 顯示所有 Question
# ──────────────────────────────────────────────
class QuestionListView(ListView):
    model = Question
    template_name = 'home.html'
    context_object_name = 'questions'
    queryset = Question.objects.all()


# ──────────────────────────────────────────────
# /question/<pk>/ ── function-based view（必須）
# ──────────────────────────────────────────────
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    choices = question.choice_set.all()
    context = {
        'question': question,
        'choices': choices,
    }
    return render(request, 'question_detail.html', context)


# ──────────────────────────────────────────────
# /stats/ ── 統計資訊
# ──────────────────────────────────────────────
def stats_view(request):
    total_questions = Question.objects.count()
    total_choices = Choice.objects.count()
    open_questions = Question.objects.filter(is_open=True).count()

    # 每題最高票選項
    questions_with_stats = []
    for q in Question.objects.all():
        choices = q.choice_set.all()          # 已依 -votes 排序
        top_choice = choices.first()
        questions_with_stats.append({
            'question': q,
            'choices': choices,
            'top_choice': top_choice,
        })

    context = {
        'total_questions': total_questions,
        'total_choices': total_choices,
        'open_questions': open_questions,
        'questions_with_stats': questions_with_stats,
    }
    return render(request, 'stats.html', context)
