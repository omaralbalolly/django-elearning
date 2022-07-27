from django.db import models
from users.models import User


class Subject(models.Model):
    name = models.CharField(max_length=20, null=True, unique=True)
    desc = models.TextField(verbose_name='Description', null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    subject = models.ForeignKey(Subject, related_name='subjects', on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(User, related_name='teachers', on_delete=models.SET_NULL, null=True)
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
