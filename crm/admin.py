from django.contrib import admin
from .models import Task, Review


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    search_fields = ("title",)
    list_filter = ("created",)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("reviewer_name", "reviewer_title", "task_id")
    search_fields = ("reviewer_name", "reviewer_title")
    list_filter = ("task",)


admin.site.register(Task, TaskAdmin)
admin.site.register(Review, ReviewAdmin)
