from .models import Post, CompanyComment, Meeting
from django.contrib.auth.models import User


def companies(request):
    ctx = {
        'companies': Post.objects.all(),
        'comments': CompanyComment.objects.all(),
        'users': User.objects.all(),
        'meetings': Meeting.objects.all(),
    }
    return ctx