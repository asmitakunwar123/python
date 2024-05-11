from django.db import models
from author.models import Author
# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=255,null=False,blank=False)
	author = models.OneToOneField(Author, on_delete=models.CASCADE, null=False, blank=False)


	def __str__(self):
		return self.title


class Book2(models.Model):
	title = models.CharField(max_length=255, null=False, blank=False)
	author = models.ForeignKey(
		Author, on_delete=models.CASCADE, null=False, blank=False)

	def __str__(self):
		return self.title
