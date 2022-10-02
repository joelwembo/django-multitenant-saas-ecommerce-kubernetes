from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
    lastest_question_list = Post.objects.all()
    context = {'latest_posts': lastest_question_list}
    return render(request, 'blog/index.html', context)
