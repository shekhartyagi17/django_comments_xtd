from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from .models import Comment, CustomXtdComment




class CustomXtdCommentSerializer(serializers.ModelSerializer):
    """
    Serializer for CustomXtdComment model using django-comments-xtd
    """
    comments = serializers.CharField(source='comment', help_text="Comment content")
    created_at = serializers.DateTimeField(source='submit_date', read_only=True)
    updated_at = serializers.DateTimeField(source='submit_date', read_only=True)
    
    class Meta:
        model = CustomXtdComment
        fields = ['id', 'application_id', 'comments', 'created_at', 'updated_at', 
                 'user_name', 'user_email', 'is_public', 'is_removed']
        read_only_fields = ['id', 'created_at', 'updated_at', 'submit_date', 'site', 'content_type', 'object_pk']

    def validate_application_id(self, value):
        """
        Validate application_id field
        """
        if not value.strip():
            raise serializers.ValidationError("Application ID cannot be empty.")
        return value

    def validate_comments(self, value):
        """
        Validate comments field
        """
        if not value.strip():
            raise serializers.ValidationError("Comments cannot be empty.")
        return value

    def create(self, validated_data):
        """
        Create a new CustomXtdComment instance
        """
        # Extract comment content from validated_data
        comment_content = validated_data.pop('comment', '')
        
        # Set default values for required django-comments-xtd fields
        validated_data.update({
            'comment': comment_content,
            'site': Site.objects.get_current(),
            'content_type': ContentType.objects.get_for_model(Comment),  # Use Comment as dummy content type
            'object_pk': '1',  # Use dummy object pk
            'is_public': True,
            'is_removed': False,
        })
        
        # Set default user info if not provided
        if not validated_data.get('user_name'):
            validated_data['user_name'] = 'Anonymous'
        if not validated_data.get('user_email'):
            validated_data['user_email'] = 'anonymous@example.com'
        
        return super().create(validated_data)


# class CommentSerializer(serializers.ModelSerializer):
#     """
#     Serializer for simple Comment model
#     """
    
#     class Meta:
#         model = Comment
#         fields = ['id', 'application_id', 'comments', 'created_at', 'updated_at']
#         read_only_fields = ['id', 'created_at', 'updated_at']

#     def validate_application_id(self, value):
#         """
#         Validate application_id field
#         """
#         if not value.strip():
#             raise serializers.ValidationError("Application ID cannot be empty.")
#         return value

#     def validate_comments(self, value):
#         """
#         Validate comments field
#         """
#         if not value.strip():
#             raise serializers.ValidationError("Comments cannot be empty.")
#         return value