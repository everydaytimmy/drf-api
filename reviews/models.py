from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

class Review(models.Model):
  reviewer = models.ForeignKey(get_user_model(), on_delete=CASCADE)
  title = models.CharField(max_length=256)
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
