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
        
        section_blog_list = []
        sections = Blog.objects.all().values_list('section_id', flat=True).distinct()
        for section in sections:
            blog = Blog.objects.filter(section_id=section)
            section_list = {
                "section_id": section,
                "section_name": blog[0].section_name,
                "blog_list": ListBlogSerializer(blog, many=True).data
            }
            section_blog_list.append(section_list)

        section_blog = {
            "section_and_blog_list": section_blog_list
        }

        return Response(section_blog)


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