# Generated by Django 4.0.6 on 2022-08-02 07:02

from django.db import migrations, models
import django.db.models.deletion
import utils.helping_functions
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
                ('description', models.TextField(null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=utils.helping_functions.get_assignment_file_path)),
                ('open_time', models.DateTimeField(null=True)),
                ('close_time', models.DateTimeField(null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(null=True, upload_to=utils.helping_functions.get_assignment_submission_path)),
                ('grade', models.PositiveIntegerField(blank=True, null=True)),
                ('assignment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assignments.assignment')),
            ],
        ),
    ]
