from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    readonly_fields = ('votes',) #Not change this on admin site
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
        search_fields = ('question_text',)
        list_display = ('question_text','pub_date')
        inlines = [ChoiceInline, ]


admin.site.register(Question,QuestionAdmin)