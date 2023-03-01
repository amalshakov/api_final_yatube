from django.contrib import admin

from .models import Group, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    empty_value_display = '-пусто-'

    def __str__(self) -> str:
        return self.text


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
