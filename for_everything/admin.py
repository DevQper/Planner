from django.contrib import admin

from .models import Task
from .models import Blogs
from .models import Reviews



class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_create', 'date_end']


admin.site.register(Task, TaskAdmin)


class BlogsAdmin(admin.ModelAdmin):
    list_display = ["id", "name_blog", "name_user"]


admin.site.register(Blogs, BlogsAdmin)


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'parent', 'blog']


admin.site.register(Reviews, ReviewsAdmin)
