from django.contrib import admin
from django_app import models

# Register your models here.

admin.site.site_header = 'Панель управления'  # default: "Django Administration"
admin.site.index_title = 'Администрирование сайта'  # default: "Site administration"
admin.site.site_title = 'Администрирование'  # default: "Django site admin"

class ProfileAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Profile' на панели администратора
    """

    list_display = (
        'user',
        'avatar',
    )
    list_display_links = (
        'user',
    )
    # list_editable = (
    #     'user',
    # )
    list_filter = (
        'user',
        'avatar',
    )
    # filter_horizontal = (
    #     'users',
    # )
    fieldsets = (
        ('Основное', {'fields': (
            'user',
            'avatar',
        )}),
    )
    search_fields = [
        'user',
        'avatar',
    ]



admin.site.register(models.Profile, ProfileAdmin)
