from django.contrib import admin
from .models import Comment, CustomXtdComment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'application_id', 'comments_preview', 'created_at', 'updated_at']
    list_filter = ['application_id', 'created_at']
    search_fields = ['application_id', 'comments']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

    def comments_preview(self, obj):
        return obj.comments[:50] + '...' if len(obj.comments) > 50 else obj.comments
    comments_preview.short_description = 'Comments Preview'


@admin.register(CustomXtdComment)
class CustomXtdCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'application_id', 'comment_preview', 'user_name', 'user_email', 'submit_date', 'is_public']
    list_filter = ['application_id', 'submit_date', 'is_public', 'is_removed']
    search_fields = ['application_id', 'comment', 'user_name', 'user_email']
    readonly_fields = ['submit_date', 'site', 'content_type', 'object_pk']
    ordering = ['-submit_date']

    def comment_preview(self, obj):
        return obj.comment[:50] + '...' if len(obj.comment) > 50 else obj.comment
    comment_preview.short_description = 'Comment Preview'
