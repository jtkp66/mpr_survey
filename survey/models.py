from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    coordinator = models.CharField(max_length=100)
    student = models.CharField(max_length=100)
    hostfamily = models.CharField(max_length=100)
    question1 = models.TextField(blank=True)
    question2 = models.TextField(blank=True)
    question3 = models.TextField(blank=True)
    is_complete = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.coordinator
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})