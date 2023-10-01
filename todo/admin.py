from django.contrib import admin
from .models import Tag, Task
from django.utils import timezone
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'due_date', 'status')
    list_filter = ('status', 'tags')
    search_fields = ('title', 'description')
    fieldsets = (
        ('General', {
            'fields': ('title', 'description', 'status')
        }),
        ('Date and Time', {
            'fields': ('due_date',)
        }),
        ('Tags', {
            'fields': ('tags',)
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.timestamp = timezone.now()
        super().save_model(request, obj, form, change)
