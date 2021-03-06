# Generated by Django 3.0.2 on 2020-01-30 02:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinator', models.CharField(max_length=100)),
                ('is_complete', models.BooleanField(default=False)),
                ('date_of_contact', models.CharField(default='0000000', max_length=20)),
                ('student_surname', models.CharField(max_length=100)),
                ('hostfamily', models.CharField(max_length=100)),
                ('student_eng_name', models.CharField(max_length=50)),
                ('st_1', models.CharField(blank=True, max_length=20)),
                ('st_1a', models.TextField(blank=True)),
                ('st_2', models.TextField(blank=True)),
                ('st_3', models.TextField(blank=True)),
                ('st_4', models.CharField(blank=True, max_length=10)),
                ('st_4a', models.TextField(blank=True)),
                ('st_4b', models.TextField(blank=True)),
                ('st_5', models.CharField(blank=True, max_length=10)),
                ('st_5a', models.TextField(blank=True)),
                ('st_6', models.CharField(blank=True, max_length=20)),
                ('st_6a', models.TextField(blank=True)),
                ('st_6b', models.TextField(blank=True)),
                ('st_7', models.CharField(blank=True, max_length=10)),
                ('st_7a', models.CharField(blank=True, max_length=10)),
                ('st_7b', models.TextField(blank=True)),
                ('st_coordinator_comments', models.TextField(blank=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('hf_hostfamily_name', models.CharField(blank=True, max_length=100)),
                ('hf_1', models.CharField(blank=True, max_length=20)),
                ('hf_1a', models.TextField(blank=True)),
                ('hf_2', models.TextField(blank=True)),
                ('hf_3', models.CharField(blank=True, max_length=10)),
                ('hf_3a', models.TextField(blank=True)),
                ('hf_3b', models.TextField(blank=True)),
                ('hf_4', models.CharField(blank=True, max_length=10)),
                ('hf_4a', models.TextField(blank=True)),
                ('hf_4b', models.TextField(blank=True)),
                ('hf_5', models.CharField(blank=True, max_length=10)),
                ('hf_5a', models.TextField(blank=True)),
                ('hf_6', models.CharField(blank=True, max_length=10)),
                ('hf_6a', models.TextField(blank=True)),
                ('hf_7', models.CharField(blank=True, max_length=20)),
                ('hf_7a', models.TextField(blank=True)),
                ('hf_coordinator_comments', models.TextField(blank=True)),
                ('sch_school_name', models.CharField(max_length=50)),
                ('sch_student_name', models.CharField(max_length=100)),
                ('sch_1a', models.CharField(max_length=100)),
                ('sch_1b', models.TextField(blank=True)),
                ('sch_2', models.CharField(blank=True, max_length=20)),
                ('sch_2a', models.TextField(blank=True)),
                ('sch_3', models.CharField(blank=True, max_length=10)),
                ('sch_3a', models.TextField(blank=True)),
                ('sch_4', models.CharField(blank=True, max_length=10)),
                ('sch_4a', models.IntegerField(default=0)),
                ('sch_4b', models.CharField(blank=True, max_length=10)),
                ('sch_4c', models.TextField(blank=True)),
                ('sch_5', models.CharField(blank=True, max_length=10)),
                ('sch_5a', models.CharField(max_length=100)),
                ('sch_6', models.CharField(blank=True, max_length=10)),
                ('sch_classes_grades', models.TextField(blank=True)),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
