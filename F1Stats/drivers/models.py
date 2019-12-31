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

	career_wins = models.IntegerField(default=0)
	career_podiums = models.IntegerField(default=0)
	career_poles = models.IntegerField(default=0)
	career_points = models.IntegerField(default=0)
	career_seasons = models.IntegerField(default=0)
	career_races = models.IntegerField(default=0)

	season_points = models.IntegerField(default=0)
	season_position = models.IntegerField(default=0)
	season_wins = models.IntegerField(default=0)
	season_podiums = models.IntegerField(default=0)
	season_avg_overtakes = models.FloatField(default=0)
	season_beat_teammate_rate = models.IntegerField(default=0)
	season_DNF_rate = models.IntegerField(default=0)




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
