from django.contrib import admin
from .models import Boys, Girls, Parent

class BoysInline(admin.TabularInline):
    model = Boys
    extra = 1
    
    

class GirlsInline(admin.TabularInline):
    extra = 1
    model = Girls


@admin.register(Parent)
class ParentModelAdmin(admin.ModelAdmin):
    inlines = [BoysInline, GirlsInline]
    list_display = ('full_name')
    
    def formatted_time(self, obj):
        if obj.boys.exists():
            return obj.boys.first().time.strftime("%Y-%m-%d %H:%M:%S.%f")
        elif obj.girls.exists():
            return obj.girls.first().time.strftime("%Y-%m-%d %H:%M:%S.%f")
        else:
            return "No time available"
    formatted_time.short_description = 'Formatted Time'  # Задаем название для отображения в административной панели
    
    list_display = ('id', 'formatted_time')  # Добавляем отформатированное время в список отображаемых полей
    # Дополнительные настройки админист