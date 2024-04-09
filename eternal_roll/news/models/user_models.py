from django.contrib.auth.models import AbstractUser
from django.db import models	

# from django.contrib.auth.models import AbstractUser
# AbstractUser.set_password

class User(AbstractUser):
	time_played = models.TimeField(auto_now=True)
	description = models.TextField()
	user_photo = models.ImageField(upload_to="photos/", blank=True, null=True) #/%Y/%m/%d для создания подкаталогов для удобства
	# запись в фото хранит только путь, что бы работа джанго была корректной нужно настроить MEDIA_ROOT MEDIA_URL
