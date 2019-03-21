from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100)
	content = models.TextField()
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.question