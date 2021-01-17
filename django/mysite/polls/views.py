from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        最後に公開された5つの質問を返します（将来公開される予定の質問は含まれません）。
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
            まだ公開されていない質問は除外します。
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 質問投票フォームを再表示します。
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "選択していません。",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POSTデータを正常に処理した後は、常にHttpResponseRedirectを返します。# これにより、ユーザーが[戻る]ボタンを押した場合にデータが2回投稿されるのを防ぎます。
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
