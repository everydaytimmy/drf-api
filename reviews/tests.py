from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Review

class ReviewTests(TestCase):

  @classmethod
  def setUpTestData(cls):
      testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
      testuser1.save()

      test_review = Review.objects.create(
        reviewer = testuser1,
        title =  'waffles',
        body = 'these waffles are good',
      )
      test_review.save()

  def test_review_content(self):
    review = Review.objects.get(id=1)
    actual_reviewer = str(review.reviewer)
    actual_title = review.title
    actual_body = review.body

    expected_reviewer = 'testuser1'
    expected_title = 'waffles'
    expected_body = 'these waffles are good'

    self.assertEqual(actual_reviewer, expected_reviewer)
    self.assertEqual(actual_title, expected_title)
    self.assertEqual(actual_body, expected_body)


