from django.shortcuts import render, get_object_or_404
from utils.decorators import login_required_message_and_redirect


# Create your views here.
@login_required_message_and_redirect
def course_page(request, course_id):
    user_courses = request.user.courses
    course = get_object_or_404(user_courses, id=course_id)
    resources = course.resources.filter(active=True).order_by('-add_time')
    context = {'course': course, 'resources':resources, 'nav': 'courses'}
    return render(request, 'course.html', context)


@login_required_message_and_redirect
def courses_page(request):
    context = {'nav': 'courses'}
    return render(request, 'courses.html', context)
