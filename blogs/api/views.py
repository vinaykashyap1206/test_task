# django imports
from django.http import Http404

# rest-framework imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# local imports
from blogs.models import Blog
from blogs.api.serializers import ListBlogSerializer, UpdateBlogSerializer


class ListBlogView(APIView):
    '''
        Api to list blogs
    '''
    def get(self, request, format=None):

        blogs = {}
        sections = Blog.objects.all().values_list('section', flat=True).distinct()
        for section in sections:
            blog = Blog.objects.filter(section=section)
            blogs[section] = ListBlogSerializer(blog, many=True).data

        return Response(blogs)


class UpdateBlogView(APIView):
    '''
        Api to update blog checkmark
    '''
    def get_object(self, pk):
        
        try:
            return Blog.objects.get(pk=pk)
        except Exception as e:
            raise Http404

    def put(self, request, pk, format=None):

        blog = self.get_object(pk)
        serializer = UpdateBlogSerializer(blog, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)