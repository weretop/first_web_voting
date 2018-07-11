from django.contrib import admin
from .models import *


class ChoiceInLine(admin.TabularInline):
    model = Choicing
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
         {'fields': ['question_txt']}
         ),
        (
            'Date information',
         {'fields': ['pub_date'], 'classes': ['collapse']}
         ),
    ]
    inlines = [ChoiceInLine, ]
    list_display = ('question_txt','pub_date')


admin.site.register(Questions, QuestionAdmin)
admin.site.register(Choicing)



# Register your models here.
