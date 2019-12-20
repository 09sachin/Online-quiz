from django.contrib import admin
from .models import QuizExpiryTime, QuizSubmissionTime, QuizTimeJavascript

# Register your models here.
admin.site.register(QuizExpiryTime)
admin.site.register(QuizSubmissionTime)
admin.site.register(QuizTimeJavascript)
