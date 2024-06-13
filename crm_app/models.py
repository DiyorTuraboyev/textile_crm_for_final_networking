from django.db import models


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	type = models.CharField(max_length=50)
	color = models.CharField(max_length=20)
	category = models.CharField(max_length=50)
	zipcode = models.CharField(max_length=20)
	available = models.BooleanField(default=False)
	price = models.IntegerField()

	def __str__(self):
		return(f"{self.name} {self.type}")
