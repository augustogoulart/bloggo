from django.conf import settings


def show_toolbar(request):
    return not request.is_ajax() and settings.DEBUG
