from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    # Student Progress Report
    coordinator = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)
    date_of_contact = models.CharField(max_length=20, default='0000000')
    student_surname = models.CharField(max_length=100)
    hostfamily = models.CharField(max_length=100)
    student_eng_name = models.CharField(max_length=50)
    st_1 = models.CharField(max_length=20, blank=True)
    st_1a = models.TextField(blank=True)
    st_2 = models.TextField(blank=True)
    st_3 = models.TextField(blank=True)
    st_4 = models.CharField(max_length=10, blank=True)
    st_4a = models.TextField(blank=True)
    st_4b = models.TextField(blank=True)
    st_5 = models.CharField(max_length=10, blank=True)
    st_5a = models.TextField(blank=True)
    st_6 = models.CharField(max_length=20, blank=True)
    st_6a = models.TextField(blank=True)
    st_6b = models.TextField(blank=True)
    st_7 = models.CharField(max_length=10, blank=True)
    st_7a = models.CharField(max_length=10, blank=True)
    st_7b = models.TextField(blank=True)
    st_coordinator_comments = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_posted = models.DateTimeField(default=timezone.now)
    # Host Family Progress Report
    hf_hostfamily_name = models.CharField(max_length=100, blank=True)
    hf_1 = models.CharField(max_length=20, blank=True)
    hf_1a = models.TextField(blank=True)
    hf_2 = models.TextField(blank=True)
    hf_3 = models.CharField(max_length=10, blank=True)
    hf_3a = models.TextField(blank=True)
    hf_3b = models.TextField(blank=True)
    hf_4 = models.CharField(max_length=10, blank=True)
    hf_4a = models.TextField(blank=True)
    hf_4b = models.TextField(blank=True)
    hf_5 = models.CharField(max_length=10, blank=True)
    hf_5a = models.TextField(blank=True)
    hf_6 = models.CharField(max_length=10, blank=True)
    hf_6a = models.TextField(blank=True)
    hf_7 = models.CharField(max_length=20, blank=True)
    hf_7a = models.TextField(blank=True)
    hf_coordinator_comments = models.TextField(blank=True)
    # School Progress Report
    sch_school_name = models.CharField(max_length=50)
    sch_student_name = models.CharField(max_length=100)
    sch_1a = models.CharField(max_length=100)
    sch_1b = models.TextField(blank=True)
    sch_2 = models.CharField(max_length=20, blank=True)
    sch_2a = models.TextField(blank=True)
    sch_3 = models.CharField(max_length=10, blank=True)
    sch_3a = models.TextField(blank=True)
    sch_4 = models.CharField(max_length=10, blank=True)
    sch_4a = models.IntegerField(default=0)
    sch_4b = models.CharField(max_length=10, blank=True)
    sch_4c = models.TextField(blank=True)
    sch_5 = models.CharField(max_length=10, blank=True)
    sch_5a = models.CharField(max_length=100)
    sch_6 = models.CharField(max_length=10, blank=True)
    sch_classes_grades = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.coordinator

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
