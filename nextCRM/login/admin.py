from django.contrib import admin
from login.models import Post, Friend, CompanyComment

# Register your models here.
admin.site.register(Post)
admin.site.register(CompanyComment)
admin.site.register(Friend) #this materializes Friend model in admin panel