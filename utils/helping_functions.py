import os


def get_resource_path(instance, filename):
    return os.path.join('courses', str(instance.course.id), 'resources', filename)


def get_user_image_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.username, ext)
    return os.path.join('users', filename)


def get_assignment_file_path(instance, filename):
    return os.path.join('assignments', str(instance.id), 'files', filename)


def get_assignment_submission_path(instance, filename):
    return os.path.join('assignments', str(instance.assignment.id), 'submissions', filename)


def seconds_to_text(seconds):
    ratios = {
        'decades': 311040000,  # 60 * 60 * 24 * 30 * 12 * 10
        'years': 31104000,  # 60 * 60 * 24 * 30 * 12
        'months': 2592000,  # 60 * 60 * 24 * 30
        'days': 86400,  # 60 * 60 * 24
        'hours': 3600,  # 60 * 60
        'minutes': 60,  # 60
        'seconds': 1  # 1
    }

    texts = []
    for ratio in ratios:
        result, seconds = divmod(seconds, ratios[ratio])
        if result:
            if result == 1:
                ratio = ratio.rstrip('s')
            texts.append(f'{result} {ratio}')
    texts = texts[:2]
    if not texts:
        return f'0 {list(ratios)[-1]}'
    text = ', '.join(texts)
    if len(texts) > 1:
        index = text.rfind(',')
        text = f'{text[:index]} and{text[index + 1:]}'
    return text
