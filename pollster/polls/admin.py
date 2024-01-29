from django.contrib import admin

from .models import Question, Choice


# Change the site description, header...
admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the pollster admin area!"


# Import Question and Choice to Admin Portal (C1: Question and Choices are managed in separate sections)
# admin.site.register(Question)
# admin.site.register(Choice)


# Import Question and Choice to Admin Portal (C2: Question and Choices are managed in same section, click on Question to see the list of Choices)
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
