from django.contrib import admin

# Register your models here.
from .models import Test, Question, Answer, TestQuestion, StudentTest

admin.site.register(Question)
admin.site.register(Answer)

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0


# Test admin
class QuestionInline(admin.TabularInline):
    model = Question
    inlines = [AnswerInline]
    extra = 0


class TestAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Test, TestAdmin)
