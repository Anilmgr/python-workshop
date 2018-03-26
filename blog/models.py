from django.db import models

# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length = 150)
	body = models.TextField()
	auther = models.CharField(max_length = 100)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title