from django.contrib import admin
from .models import Recipe, Comment, Rating, Category
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('recipe_name', 'slug', 'status')
    search_fields = ['recipe_name']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('recipe_name',)}
    summernote_fields = ('ingredients','instructions')



admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Rating)