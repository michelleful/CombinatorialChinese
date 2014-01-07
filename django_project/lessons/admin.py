from django.contrib import admin

# Register your models here.
from lessons.models import Page, Text, Lesson

class PageAdmin(admin.ModelAdmin):
    pass

class TextAdmin(admin.ModelAdmin):
    pass

class LessonAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Page)
admin.site.register(Text)
admin.site.register(Lesson)
