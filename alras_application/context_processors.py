
from django.contrib.auth.models import User

def message_processor(request):
    if request.user.is_authenticated:
        no_msgs = 1
    else:
        no_msgs = 0
    return {
        'message' : no_msgs
    }