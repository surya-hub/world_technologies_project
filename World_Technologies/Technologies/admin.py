from django.contrib import admin

from .models import Courses

class CourseAdmin(admin.ModelAdmin):
    list_display = ['cname','trainer_name','start_date','content',
        'photo']

admin.site.register(Courses,CourseAdmin)

