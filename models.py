from __future__ import unicode_literals

from django.db import models

# Create your models here.
class EmailInvitation(models.Model) :
	From  = models.EmailField(max_length = 70)
	To = models.EmailField(max_length = 70)
	Subject = models.CharField(max_length = 200)
	uniqueCode = models.IntegerField()
	eventName = models.CharField(max_length = 100)


	def _str_(self):
		return self.To