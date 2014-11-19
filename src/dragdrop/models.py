from django.db import models
from dragdrop.files import get_path
from django.contrib.auth.models import User
from drinker.models import Drinker
from django.conf import settings

def _upload_path(instance, filename):
	return instance.get_upload_path(filename)

class UploadFile(models.Model):
	file = models.ImageField(upload_to=_upload_path)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return "{0} - {1}".format(self.user, self.file)

	def get_upload_path(self, filename):
		return "user_"+str(self.user.username)+"/"+filename
#		return str(self.user.username)+"_"+filename






# THIS IS FOR RACKSPACE CLOUD STORAGE
# 
# from backends.mosso import cloudfiles_upload_to

# class SomeKlass(models.Model):
#     some_field = models.ImageField(upload_to=cloudfiles_upload_to)



# from backends.mosso import CloudFilesStorage, cloudfiles_upload_to

# cloudfiles_storage = CloudFilesStorage()

# class SomeKlass(models.Model):
#     some_field = models.ImageField(storage=cloudfiles_storage,
#                                    upload_to=cloudfiles_upload_to)
