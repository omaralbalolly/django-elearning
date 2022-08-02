from django.db import models
from courses.models import Course
from utils.helping_functions import get_assignment_file_path, get_assignment_submission_path
from users.models import User
from django.utils import timezone
from utils.helping_functions import seconds_to_text
import uuid


# Create your models here.
class Assignment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name='assignments')
    description = models.TextField(null=True)
    file = models.FileField(upload_to=get_assignment_file_path, null=True, blank=True)
    open_time = models.DateTimeField(null=True)
    close_time = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.course}'

    @property
    def is_open(self):
        return self.close_time > timezone.now() > self.open_time

    @property
    def remaining_time(self):
        if self.is_open:
            time = seconds_to_text((self.close_time - timezone.now()).seconds)
            return time
        return None


class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, null=True, on_delete=models.CASCADE)
    student = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=get_assignment_submission_path, null=True)
    grade = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['assignment', 'student'],
                name='assignment_student_unique',
            ),
        ]
