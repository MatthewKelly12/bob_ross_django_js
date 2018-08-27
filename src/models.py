from django.db import models

# birthday model
class Birthday(models.Model):
	name = models.CharField(max_length=50)
	date = models.CharField(max_length=50)
	time = models.DateField(auto_now=False, auto_now_add=False)
	greeting = models.CharField(max_length=100)

	def __str__(self):
		return f'{self.name}'

	class Meta:
		db_table = "birthdays"
# date
# time
# greeting

# in DB browser add 3 birdtday instances
# make url config
# make a view for sending back birdtday data
