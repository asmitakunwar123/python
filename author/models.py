from django.db import models


class Author(models.Model):
	First_name=models.CharField(max_length= 250,null=False, blank=False)
	last_name = models.CharField(max_length= 250,null=False, blank=False)
	age= models.IntegerField(default=18)
	created_at = models.DateTimeField(null=False, blank=False)

# def __str__(self):
# 	return f"{self.frist_name} {self.last_name}"
def __str__(self):
        return f"{self.First_name} {self.last_name}"