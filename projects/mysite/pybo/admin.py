from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Answer


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Answer)
admin.site.register(Question, QuestionAdmin)
