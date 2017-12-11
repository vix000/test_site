from .models import Post, CompanyComment
from django.contrib.auth.models import User


def companies(request):
    ctx = {
        'companies': Post.objects.all(),
        'comments': CompanyComment.objects.all(),
        'users': User.objects.all(),
    }
    return ctx