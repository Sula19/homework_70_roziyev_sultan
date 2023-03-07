from django.contrib import admin
from webapp.models import Tasks


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'description', 'status', 'created', 'updated')
    list_filter = ('id', 'summary', 'description', 'status', 'type',  'created', 'updated')
    search_fields = ('summary', 'description' 'status', 'type')
    fields = ('summary', 'description', 'status', 'type',  'created', 'updated')
    readonly_fields = ('id', 'created', 'updated')


admin.site.register(Tasks, TaskAdmin)