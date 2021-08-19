from .models import Question
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello world!')


def questions(request):
    return HttpResponse(Question.objects.all())
