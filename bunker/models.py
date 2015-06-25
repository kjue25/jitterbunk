from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils import timezone

class Bunk(models.Model):
	from_user = models.ForeignKey(User, related_name="from")
	to_user = models.ForeignKey(User, related_name="to")
	time = models.DateTimeField('bunk time', default=timezone.now())
	def __unicode__(self):
		bunk_str = self.from_user.username +  " bunked " + self.to_user.username
		return bunk_str 

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	#ImageField params may need to be fixed
	photo = models.ImageField('path', default="background.gif", upload_to="images/") 
	def __unicode__(self):
		return self.user.username

class BunkForm(ModelForm):
	class Meta:
		model = Bunk
		fields = ['from_user', 'to_user']
		exclude = ['time']
