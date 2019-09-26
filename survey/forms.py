from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('coordinator', 'student', 'hostfamily', 'question1', 'question2', 'question3', 'is_complete')
