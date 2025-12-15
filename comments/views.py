from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Comment, CustomXtdComment
from .serializers import  CustomXtdCommentSerializer

# Django Comments XTD Views
class XtdCommentListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve list of extended comments or create a new extended comment using django-comments-xtd.
    """
    queryset = CustomXtdComment.objects.all()
    serializer_class = CustomXtdCommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': 'true',
                    'message': 'Extended comment created truefully ',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'status': 'error',
                'message': 'Validation failed',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {
                'status': 'true',
                'message': 'Extended comments retrieved truefully',
                'data': serializer.data,
                'count': len(serializer.data)
            },
            status=status.HTTP_200_OK
        )



@api_view(['GET'])
def xtd_comments_by_application(request, application_id):
    """
    API view to get extended comments filtered by application_id
    """
    try:
        comments = CustomXtdComment.objects.filter(application_id=application_id)
        serializer = CustomXtdCommentSerializer(comments, many=True)
        return Response(
            {
                'status': 'true',
                'message': f'Extended comments for application {application_id} retrieved truefully',
                'data': serializer.data,
                'count': len(serializer.data)
            },
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {
                'status': 'error',
                'message': str(e)
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class CommentListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve list of comments or create a new comment.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': 'true',
                    'message': 'Comment created truefully',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'status': 'error',
                'message': 'Validation failed',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {
                'status': 'true',
                'message': 'Comments retrieved truefully',
                'data': serializer.data,
                'count': len(serializer.data)
            },
            status=status.HTTP_200_OK
        )


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a comment instance.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            {
                'status': 'true',
                'message': 'Comment retrieved truefully',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )


@api_view(['GET'])
def comments_by_application(request, application_id):
    """
    API view to get comments filtered by application_id
    """
    try:
        comments = Comment.objects.filter(application_id=application_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(
            {
                'status': 'true',
                'message': f'Comments for application {application_id} retrieved truefully',
                'data': serializer.data,
                'count': len(serializer.data)
            },
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {
                'status': 'error',
                'message': str(e)
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


