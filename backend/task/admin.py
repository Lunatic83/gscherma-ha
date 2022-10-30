from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'content')


admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)
