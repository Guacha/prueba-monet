from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline

# Register your models here.
from .models import Test, Question, Answer, TestQuestion, StudentTest

admin.site.register(Question)
admin.site.register(Answer)


class AnswerInline(NestedStackedInline):
    model = Answer
    extra = 0


# Test admin
class QuestionInline(NestedTabularInline):
    model = Question
    inlines = [AnswerInline]
    extra = 0


class TestAdmin(NestedModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Test, TestAdmin)


