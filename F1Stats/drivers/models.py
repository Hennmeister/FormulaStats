from django.db import models

# Create your models here.
class Constructor(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name


class Driver(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	constructor = models.ForeignKey(Constructor, on_delete=models.CASCADE)

	def __str__(self):
		return self.last_name

#	date_of_birth = models.DateTimeField()

	# @property
	# def age(self) -> int:
	# 	import datetime
	# 	today = datetime.date.today()
	# 	years = today.year - self.date_of_birth.year
	# 	if today.month < self.date_of_birth.month or (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
	# 		years -= 1
	# 	return years
