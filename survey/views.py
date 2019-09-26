from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import PostForm
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
)
from .models import Post


def index(request):
    posts = Post.objects.order_by('date_posted').filter(is_complete=True)

    context = {
        'posts': posts
    }

    return render(request, 'survey/surveys.html', context)        

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post
    }

    return render(request, 'survey/survey2.html', context)

def survey_new(request):

    return render(request, 'survey/survey-new2.html')

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['coordinator', 'student', 'hostfamily', 'question1', 'question2', 'question3', 'is_complete']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('dashboard')
    else:
        form = PostForm()
    return render(request, 'survey/survey-new2.html', {'form': form})


class PostDetailView(DetailView):
    model = Post

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})
