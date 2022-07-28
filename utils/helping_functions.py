import os


def get_resource_path(instance, filename):
    return os.path.join('courses', str(instance.course.id), filename)


def get_user_image_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.username, ext)
    return os.path.join('users', filename)
