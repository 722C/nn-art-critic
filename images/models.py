from django.db import models

# Create your models here.


class Image(models.Model):
	image = models.ImageField()

	def __unicode__(self):
		return self.image.name


class BetterThan(models.Model):
	better_than = models.ForeignKey(Image, related_name='better_than_rel')
	worse_than = models.ForeignKey(Image, related_name='worse_than_rel')

	def __unicode__(self):
		return u'{0} > {1}'.format(self.better_than, self.worse_than)


