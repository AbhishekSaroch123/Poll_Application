from django.contrib import admin

# Register your models here.
from .models import Question,Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # ordering the fields on admin side 1->Pub Date 2->Question Text
    # fields=['pub_date','question_text']

    fieldsets = [
        # name of section :{field:question_text}
        ('Add Your Question Here',{'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    # create a search field that is going to search the questions
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
