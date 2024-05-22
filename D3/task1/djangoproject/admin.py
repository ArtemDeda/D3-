from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_published')
    readonly_fields = ('date_published',)


admin.site.register(News, NewsAdmin)