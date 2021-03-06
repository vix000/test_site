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
	categories = (
		('Food', 'Food'),
		('Transport', 'Transport'),
		('IT', 'IT'),
		('Logistics', 'Logistics'),
		('Other', 'Other'),
	)
	category = models.CharField(max_length=9, choices=categories, blank=True)
	image = models.ImageField(upload_to='profile_image', blank=True, null=True) #blank means it can be optional

	def __str__(self):
		return self.post


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



class CompanyComment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    user = models.ForeignKey(User)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default = False)

    def approved(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.user



class Meeting(models.Model):
	title = models.CharField(max_length=100)
	company_name = models.ForeignKey(Post)
	meeting_date = models.DateTimeField()
	details = models.TextField(max_length=250)
	created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, null=True, default=User)
	def __str__(self):
		return self.title
