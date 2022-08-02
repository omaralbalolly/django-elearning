from django.db import models
from users.models import User
import os
from django.utils.timezone import datetime
from utils.helping_functions import get_resource_path
from django.conf import settings


class Subject(models.Model):
    name = models.CharField(max_length=20, null=True, unique=True)
    desc = models.TextField(verbose_name='Description', null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(User, related_name="courses", through="Enrollment")

    def __str__(self):
        return f'{self.subject} - {self.teacher}'


class Enrollment(models.Model):
    student = models.ForeignKey(User, related_name="enrollments", on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    grade = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return f'{self.student} - {self.course}'

    class Meta:
        unique_together = ('student', 'course')


class Resource(models.Model):
    name = models.CharField(max_length=50, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name='resources')
    file = models.FileField(upload_to=get_resource_path, null=True)
    add_time = models.DateTimeField(default=datetime.now)
    active = models.BooleanField(default=True, null=True)

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.name
