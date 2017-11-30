from django.contrib import admin
from login.models import Post, Friend

# Register your models here.
admin.site.register(Post)
admin.site.register(Friend) #this materializes Friend model in admin panel