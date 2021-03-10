from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
	"""Any user defined topic"""
	text = models.CharField(max_length = 200)
	date_added = models.DateTimeField(auto_now_add = True)
	owner = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		"""Magic method to return the string representation of the model"""
		return self.text

class Entry(models.Model):
	"""The entries for every topic"""
	topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)


	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Doesn't display the whole entry"""
		return self.text[:50] + "..."