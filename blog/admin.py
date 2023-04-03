from django.contrib import admin
from blog.models import Post, User, Category, Tags, Comments

import csv
from django.http import HttpResponse

# class ExportCsvMixin:
def export_as_csv(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)
    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])
    return response


class PostAdmin(admin.ModelAdmin):
    list_filter = ['category','tag','author','created_date','published_date']
    actions = [export_as_csv]
    list_display = ('title', 'author', 'thumbnail', 'published_date')
    search_fields = ['title']
    filter_horizontal = ('tag',)
    autocomplete_fields = ['author','category']


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['title']
    search_fields = ['category']
    

class UserAdmin(admin.ModelAdmin):
    list_filter = ['first_name','last_name','email','username','city','country','gender']
    search_fields = ['first_name','last_name','email','username','city','country','gender']


class TagsAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']


class CommentsAdmin(admin.ModelAdmin):
    list_filter = ['name','email','comment','created_date']
    search_fields = ['name','email','comment','created_date']
    autocomplete_fields = ['post']


admin.site.register(Post,PostAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tags,TagsAdmin)
admin.site.register(Comments,CommentsAdmin)