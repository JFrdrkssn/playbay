from django.contrib import admin
from .models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    """
    The Category of posts of the admin page
    """

    list_display = ('name',)
    search_fields = ['name']
    list_filter = ('name',)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    The Blog Post section of the admin page
    """

    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    The Comment section of the admin page
    """

    list_display = ('user', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('user', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
