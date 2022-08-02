from django.shortcuts import render, get_object_or_404, redirect
from .models import Assignment, AssignmentSubmission
from django.core.exceptions import PermissionDenied
from .forms import AssignmentSubmissionForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils import timezone
from utils.decorators import login_required_message_and_redirect


@login_required_message_and_redirect
def assignment_page(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id, active=True)
    if assignment.course not in request.user.courses.all():
        raise PermissionDenied()
    try:
        submission = AssignmentSubmission.objects.get(student=request.user, assignment=assignment)
    except ObjectDoesNotExist:
        submission = None

    submit_form = AssignmentSubmissionForm(data=request.POST or None, files=request.FILES or None, instance=submission)
    if submit_form.is_valid():
        if not assignment.is_open:
            messages.error(request, 'The submission period has ended')
            return redirect('assignment', assignment_id)
        submission = submit_form.save(commit=False)
        submission.assignment = assignment
        submission.course = assignment.course
        submission.student = request.user
        submission.time = timezone.now()
        submission.save()
        messages.success(request, 'Your submission has been saved successfully')
        return redirect('assignment', assignment_id)

    context = {'assignment': assignment, 'submit_form': submit_form, 'submission': submission}
    return render(request, 'assignment.html', context=context)
