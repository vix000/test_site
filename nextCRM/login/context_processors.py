from .models import Post, Comment


def companies(request):
    ctx = {
        'companies': Post.objects.all(),
        'comments': Comment.objects.all()
    }
    return ctx