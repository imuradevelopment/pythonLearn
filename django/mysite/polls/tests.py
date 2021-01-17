import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

"""
    テスト用のメソッドとして、test で始まるメソッドを作成する。
    データベースは各テストメソッドごとにリセット
"""

"""
modelのテスト
models.py
"""
class QuestionModelTests(TestCase):

  def test_was_published_recently_with_future_question(self):
      """
      テスト用のメソッドとして、test で始まるメソッドを作成。
      was_published_recently（）は、pub_dateが将来の質問に対してFalseを返します。
      """
      time = timezone.now() + datetime.timedelta(days=30)
      future_question = Question(pub_date=time)
      self.assertIs(future_question.was_published_recently(), False)

  def test_was_published_recently_with_old_question(self):
      """
      was_published_recently（）は、pub_dateが1日より古い質問に対してFalseを返します。
      """
      time = timezone.now() - datetime.timedelta(days=1, seconds=1)
      old_question = Question(pub_date=time)
      self.assertIs(old_question.was_published_recently(), False)

  def test_was_published_recently_with_recent_question(self):
      """
      was_published_recently（）は、pub_dateが月末以内の質問に対してTrueを返します。
      """
      time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
      recent_question = Question(pub_date=time)
      self.assertIs(recent_question.was_published_recently(), True)


"""
Viewのテスト
views.py
"""
"""IndexView"""
def create_question(question_text, days):
    """
    指定された「question_text」を使用して質問を作成し、指定された「日数」を現在までオフセットにして公開します。
    （過去に公開された質問の場合は公表、まだ公開されていない質問の場合は非公表）。
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        質問が存在しない場合は、適切なメッセージが表示されます。
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "投票は利用できません。")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        過去にpub_dateを使用した質問は、インデックスページに表示されます。
        """
        create_question(question_text="過去の質問", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: 過去の質問>']
        )

    def test_future_question(self):
        """
        今日以降のpub_dateを含む質問は、インデックスページに表示されません。
        """
        create_question(question_text="未来の質問", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "投票は利用できません。")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        過去と未来の両方の質問が存在する場合でも、過去の質問のみが表示されます。
        """
        create_question(question_text="過去の質問", days=-30)
        create_question(question_text="未来の質問", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: 過去の質問>']
        )

    def test_two_past_questions(self):
        """
        質問のインデックスページには、複数の質問が表示される場合があります。
        """
        create_question(question_text="過去の質問 1", days=-30)
        create_question(question_text="過去の質問 2", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: 過去の質問 2>', '<Question: 過去の質問 1>']
        )


"""DetailView"""
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        未来のpub_dateを含む質問の詳細ビューは、404notfoundを返します。
        """
        future_question = create_question(
            question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        過去のpub_dateを使用した質問の詳細ビューは、質問のテキストが表示されます。
        """
        past_question = create_question(
            question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
