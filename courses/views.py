from django.shortcuts import render
from .models import Course
from users.models import User
from utils.decorators import login_required_message_and_redirect


# Create your views here.
@login_required_message_and_redirect
def course_page(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {'course': course}
    return render(request, 'course.html', context)


@login_required_message_and_redirect
def courses_page(request):
    courses_ = request.user.courses.all()
    context = {'courses': courses_, 'nav': 'courses'}
    return render(request, 'courses.html', context)


def test(request):
    return render(request, 'test.html')
