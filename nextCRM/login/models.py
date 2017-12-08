from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Post(models.Model):
	post = models.CharField(max_length=500)
	location = models.CharField(max_length=500, default=None)
	# phone_number = PhoneNumberField(default=None)
	info = models.CharField(max_length=500, default='')
	user = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	image = models.ImageField(upload_to='profile_image', blank=True)

	def __str__(self):
		return self.post


class Comment(models.Model):
	class Meta:
		db_table = "comments"

	post_id = models.ForeignKey(Post, default=Post, null=True)
	author_id = models.ForeignKey(User, default=User, null=True)
	content = models.TextField(default='')

	def __str__(self):
		return self.content[0:200]




class Friend(models.Model):
	users = models.ManyToManyField(User) #all the other users
	current_user = models.ForeignKey(User, related_name='owner', null=True) #user currently logged in

	@classmethod
	def make_friend(cls, current_user, new_friend):
		friend, created = cls.objects.get_or_create(
			current_user=current_user
			)
		friend.users.add(new_friend)

	@classmethod
	def lose_friend(cls, current_user, new_friend):
		friend, created = cls.objects.get_or_create(
			current_user=current_user
			)
		friend.users.remove(new_friend)