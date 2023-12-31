from django.db import models

# Create your models here.
class Post(models.Model):
  subject = models.CharField(max_length=200)
  content = models.TextField()
  create_date = models.DateTimeField()
  modify_date = models.DateTimeField()

  def __str__(self):
    return self.subject

class Reply(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  content = models.TextField()
  create_date = models.DateTimeField()
  modify_date = models.DateTimeField()

  def __str__(self):
    return f"[{self.post.subject}] {self.content}"