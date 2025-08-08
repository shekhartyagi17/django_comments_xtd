from django.db import models
from django.utils import timezone
from django_comments_xtd.models import XtdComment


class CustomXtdComment(XtdComment):
    """
    Extended comment model with application_id field
    """
    application_id = models.CharField(max_length=255, help_text="Application identifier", blank=True)

    class Meta:
        verbose_name = 'Extended Comment'
        verbose_name_plural = 'Extended Comments'

    def __str__(self):
        return f"Comment {self.id} for {self.application_id}: {self.comment[:50]}..."


# Keep the original Comment model for backward compatibility
class Comment(models.Model):
    """
    Simple comment model for basic API usage
    """
    application_id = models.CharField(max_length=255, help_text="Application identifier")
    comments = models.TextField(help_text="Comment content")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Simple Comment'
        verbose_name_plural = 'Simple Comments'

    def __str__(self):
        return f"Comment {self.id} for {self.application_id}: {self.comments[:50]}..."
