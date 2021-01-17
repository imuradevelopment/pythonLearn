import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

"""テスト用のメソッドとして、test で始まるメソッドを作成。"""
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
