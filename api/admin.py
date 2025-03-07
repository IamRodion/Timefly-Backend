from django.contrib import admin
from .models import Worker, TimeEntry

# Register your models here.

# admin.site.register(Book)

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    """
    Datos del modelo Worker:
    firstname
    lastname
    email
    employee_id
    department
    hire_date
    active
    """
    list_display = ('id', 'firstname', 'lastname', 'email', 'employee_id', 'department', 'hire_date', 'active')
    list_display_links = ('employee_id',)
    list_filter = ('hire_date', 'department', 'active')
    list_per_page = 10
    ordering = ('id',)
    search_fields = ('firstname', 'lastname', 'email', 'employee_id', 'department')
    #exclude = ('id', )


@admin.register(TimeEntry)
class TimeEntryAdmin(admin.ModelAdmin):
    """
    Datos del modelo TimeEntry
    worker
    time
    entry_type
    """
    list_display = ('id', 'worker', 'entry_type', 'time')
    list_display_links = ('id',)
    list_filter = ('worker', 'entry_type', 'time')
    list_per_page = 10
    ordering = ('id',)
    search_fields = ('worker', 'entry_type')