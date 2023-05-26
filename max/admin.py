from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Edition, Category

# Register your models here.

class EditionAdmin(admin.ModelAdmin):
    list_display = ('name','pub_date','photo','is_published')
    search_fields = ('name',)
    list_filter = ('name',)
    list_editable = ('is_published',)
    fields = ('name','photo')
    # prepopulated_fields = {'slug':('name',)}
    empty_value_display = '--empty--'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'img','get_img')
    prepopulated_fields = {'slug':('name',)}
    readonly_fields = ('get_img',)
    fields = ('name','slug',('img','get_img'),)

    # fieldsets = (

    #     (None, {
    #         'fields': (('img', 'get_img'),)
    #     }),

    # )


    def get_img(self,obj):
        return mark_safe(f'<img src={obj.img.url} width="50" height="60">')

    get_img.short_description = 'Категория'



admin.site.register(Edition, EditionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.site_title = 'FRee Book'
admin.site.site_header = 'Then Book'
