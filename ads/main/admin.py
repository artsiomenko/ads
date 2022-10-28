from django.contrib import admin
from .models import Ad, Rubric


class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'price', 'published', 'rubric')
    fields = (('rubric', 'author'), 'title', 'content', 'price')


admin.site.register(Ad, AdAdmin)
admin.site.register(Rubric)
